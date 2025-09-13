# Memory dump analysis


## Start

Start **searching** for **malware** inside the pcap. Use the **tools** mentioned in [[../malware-analysis.md|**Malware Analysis**]].

## [[volatility-cheatsheet.md|Volatility]]

**Volatility is the main open-source framework for memory dump analysis**. This Python tool analyzes dumps from external sources or VMware VMs, identifying data like processes and passwords based on the dump's OS profile. It's extensible with plugins, making it highly versatile for forensic investigations.

[[volatility-cheatsheet.md|**Find here a cheatsheet**]]

## Mini dump crash report

When the dump is small (just some KB, maybe a few MB) then it's probably a mini dump crash report and not a memory dump.

![[<../../../images/image (532).png>|]]

If you have Visual Studio installed, you can open this file and bind some basic information like process name, architecture, exception info and modules being executed:

![[<../../../images/image (263).png>|]]

You can also load the exception and see the decompiled instructions

![[<../../../images/image (142).png>|]]

![[<../../../images/image (610).png>|]]

Anyway, Visual Studio isn't the best tool to perform an analysis of the depth of the dump.

You should **open** it using **IDA** or **Radare** to inspection it in **depth**.

​



