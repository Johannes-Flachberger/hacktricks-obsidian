# Checklist - Linux Privilege Escalation


### **Best tool to look for Linux local privilege escalation vectors:** [[https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS|**LinPEAS**]]

### [[privilege-escalation/README.md#System Information|System Information]]

- [ ] Get **OS information**
- [ ] Check the [[privilege-escalation/README.md#Path|PATH]], any **writable folder**?
- [ ] Check [[privilege-escalation/README.md#Env Info|env variables]], any sensitive detail?
- [ ] Search for [[privilege-escalation/README.md#Kernel Exploits|kernel exploits]] **using scripts** (DirtyCow?)
- [ ] **Check** if the [[privilege-escalation/README.md#Sudo Version|sudo version is vulnerable]]
- [ ] [[privilege-escalation/README.md#Dmesg Signature Verification Failed|Dmesg signature verification failed]]
- [ ] More system enum ([[privilege-escalation/README.md#More System Enumeration|date, system stats, cpu info, printers]])
- [ ] [[privilege-escalation/README.md#Enumerate Possible Defenses|Enumerate more defenses]]

### [[privilege-escalation/README.md#Drives|Drives]]

- [ ] **List mounted** drives
- [ ] **Any unmounted drive?**
- [ ] **Any creds in fstab?**

### [[privilege-escalation/README.md#Installed Software|Installed Software]]

- [ ] **Check for**[[privilege-escalation/README.md#Useful Software| useful software]] **installed**
- [ ] **Check for** [[privilege-escalation/README.md#Vulnerable Software Installed|vulnerable software]] **installed**

### [[privilege-escalation/README.md#Processes|Processes]]

- [ ] Is any **unknown software running**?
- [ ] Is any software running with **more privileges than it should have**?
- [ ] Search for **exploits of running processes** (especially the version running).
- [ ] Can you **modify the binary** of any running process?
- [ ] **Monitor processes** and check if any interesting process is running frequently.
- [ ] Can you **read** some interesting **process memory** (where passwords could be saved)?

### [[privilege-escalation/README.md#Scheduled Jobs|Scheduled/Cron jobs?]]

- [ ] Is the [[privilege-escalation/README.md#Cron Path|PATH ]]being modified by some cron and you can **write** in it?
- [ ] Any [[privilege-escalation/README.md#Cron Using A Script With A Wildcard Wildcard Injection|wildcard ]]in a cron job?
- [ ] Some [[privilege-escalation/README.md#Cron Script Overwriting And Symlink|modifiable script ]]is being **executed** or is inside **modifiable folder**?
- [ ] Have you detected that some **script** could be or are being [[privilege-escalation/README.md#Frequent Cron Jobs|executed very frequently]]? (every 1, 2 or 5 minutes)

### [[privilege-escalation/README.md#Services|Services]]

- [ ] Any **writable .service** file?
- [ ] Any **writable binary** executed by a **service**?
- [ ] Any **writable folder in systemd PATH**?

### [[privilege-escalation/README.md#Timers|Timers]]

- [ ] Any **writable timer**?

### [[privilege-escalation/README.md#Sockets|Sockets]]

- [ ] Any **writable .socket** file?
- [ ] Can you **communicate with any socket**?
- [ ] **HTTP sockets** with interesting info?

### [[privilege-escalation/README.md#D Bus|D-Bus]]

- [ ] Can you **communicate with any D-Bus**?

### [[privilege-escalation/README.md#Network|Network]]

- [ ] Enumerate the network to know where you are
- [ ] **Open ports you couldn't access before** getting a shell inside the machine?
- [ ] Can you **sniff traffic** using `tcpdump`?

### [[privilege-escalation/README.md#Users|Users]]

- [ ] Generic users/groups **enumeration**
- [ ] Do you have a **very big UID**? Is the **machine** **vulnerable**?
- [ ] Can you [[privilege-escalation/interesting-groups-linux-pe/README.md|escalate privileges thanks to a group]] you belong to?
- [ ] **Clipboard** data?
- [ ] Password Policy?
- [ ] Try to **use** every **known password** that you have discovered previously to login **with each** possible **user**. Try to login also without a password.

### [[privilege-escalation/README.md#Writable Path Abuses|Writable PATH]]

- [ ] If you have **write privileges over some folder in PATH** you may be able to escalate privileges

### [[privilege-escalation/README.md#Sudo And Suid|SUDO and SUID commands]]

- [ ] Can you execute **any command with sudo**? Can you use it to READ, WRITE or EXECUTE anything as root? ([[https://gtfobins.github.io)|**GTFOBins**]]
- [ ] Is any **exploitable SUID binary**? ([[https://gtfobins.github.io)|**GTFOBins**]]
- [ ] Are [[privilege-escalation/README.md#Sudo Execution Bypassing Paths|sudo commands limited by path? can you bypass the restrictions]]?
- [ ] [[privilege-escalation/README.md#Sudo Command Suid Binary Without Command Path|Sudo/SUID binary without path indicated]]?
- [ ] [[privilege-escalation/README.md#Suid Binary With Command Path|SUID binary specifying path]]? Bypass
- [ ] [[privilege-escalation/README.md#Ld_Preload|LDPRELOAD vuln]]
- [ ] [[privilege-escalation/README.md#Suid Binary So Injection|Lack of .so library in SUID binary]] from a writable folder?
- [ ] [[privilege-escalation/README.md#Reusing Sudo Tokens|SUDO tokens available]]? [[privilege-escalation/README.md#Var Run Sudo Ts Less Than Username Greater Than|Can you create a SUDO token]]?
- [ ] Can you [[privilege-escalation/README.md#Etc Sudoers Etc Sudoers D|read or modify sudoers files]]?
- [ ] Can you [[privilege-escalation/README.md#Etc Ld So Conf D|modify /etc/ld.so.conf.d/]]?
- [ ] [[privilege-escalation/README.md#Doas|OpenBSD DOAS]] command

### [[privilege-escalation/README.md#Capabilities|Capabilities]]

- [ ] Has any binary any **unexpected capability**?

### [[privilege-escalation/README.md#Acls|ACLs]]

- [ ] Has any file any **unexpected ACL**?

### [[privilege-escalation/README.md#Open Shell Sessions|Open Shell sessions]]

- [ ] **screen**
- [ ] **tmux**

### [[privilege-escalation/README.md#Ssh|SSH]]

- [ ] **Debian** [[privilege-escalation/README.md#Debian Openssl Predictable Prng Cve 2008 0166|OpenSSL Predictable PRNG - CVE-2008-0166]]
- [ ] [[privilege-escalation/README.md#Ssh Interesting Configuration Values|SSH Interesting configuration values]]

### [[privilege-escalation/README.md#Interesting Files|Interesting Files]]

- [ ] **Profile files** - Read sensitive data? Write to privesc?
- [ ] **passwd/shadow files** - Read sensitive data? Write to privesc?
- [ ] **Check commonly interesting folders** for sensitive data
- [ ] **Weird Location/Owned files,** you may have access to or alter executable files
- [ ] **Modified** in last mins
- [ ] **Sqlite DB files**
- [ ] **Hidden files**
- [ ] **Script/Binaries in PATH**
- [ ] **Web files** (passwords?)
- [ ] **Backups**?
- [ ] **Known files that contains passwords**: Use **Linpeas** and **LaZagne**
- [ ] **Generic search**

### [[privilege-escalation/README.md#Writable Files|Writable Files]]

- [ ] **Modify python library** to execute arbitrary commands?
- [ ] Can you **modify log files**? **Logtotten** exploit
- [ ] Can you **modify /etc/sysconfig/network-scripts/**? Centos/Redhat exploit
- [ ] Can you [[privilege-escalation/README.md#Init Init D Systemd And Rc D|write in ini, int.d, systemd or rc.d files]]?

### [[privilege-escalation/README.md#Other Tricks|Other tricks]]

- [ ] Can you [[privilege-escalation/README.md#Nfs Privilege Escalation|abuse NFS to escalate privileges]]?
- [ ] Do you need to [[privilege-escalation/README.md#Escaping From Restricted Shells|escape from a restrictive shell]]?



