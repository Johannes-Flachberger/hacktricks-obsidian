# Crypto

This section focuses on **practical cryptography for hacking/CTFs**: how to quickly recognize common patterns, pick the right tools, and apply known attacks.

If you're here for hiding data inside files, go to the **Stego** section.

## How to use this section

Crypto challenges reward speed: classify the primitive, identify what you control (oracle/leak/nonce reuse), then apply a known attack template.

### CTF workflow
[[ctf-workflow/README.md]]

### Symmetric crypto
[[symmetric/README.md]]

### Hashes, MACs, and KDFs
[[hashes/README.md]]

### Public-key crypto
[[public-key/README.md]]

### TLS and certificates
[[tls-and-certificates/README.md]]

### Crypto in malware
[[crypto-in-malware/README.md]]

### Misc
[[ctf-misc/README.md]]

## Quick setup

- Python: `python3 -m venv .venv && source .venv/bin/activate`
- Libraries: `pip install pycryptodome gmpy2 sympy pwntools`
- SageMath (often essential for lattice/RSA/ECC): https://www.sagemath.org/

