# Checklist - Local Windows Privilege Escalation


### **Best tool to look for Windows local privilege escalation vectors:** [[https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS|**WinPEAS**]]

### [[windows-local-privilege-escalation/README.md#System Info|System Info]]

- [ ] Obtain [[windows-local-privilege-escalation/README.md#System Info|System information]]
- [ ] Search for **kernel** [[windows-local-privilege-escalation/README.md#Version Exploits|exploits using scripts]]
- [ ] Use **Google to search** for kernel **exploits**
- [ ] Use **searchsploit to search** for kernel **exploits**
- [ ] Interesting info in [[windows-local-privilege-escalation/README.md#Environment|env vars]]?
- [ ] Passwords in [[windows-local-privilege-escalation/README.md#Powershell History|PowerShell history]]?
- [ ] Interesting info in [[windows-local-privilege-escalation/README.md#Internet Settings|Internet settings]]?
- [ ] [[windows-local-privilege-escalation/README.md#Drives|Drives]]?
- [ ] [[windows-local-privilege-escalation/README.md#Wsus|WSUS exploit]]?
- [ ] [[windows-local-privilege-escalation/abusing-auto-updaters-and-ipc.md|**Third-party agent auto-updaters / IPC abuse**]]
- [ ] [[windows-local-privilege-escalation/README.md#Alwaysinstallelevated|AlwaysInstallElevated]]?

### [[windows-local-privilege-escalation/README.md#Enumeration|Logging/AV enumeration]]

- [ ] Check [[windows-local-privilege-escalation/README.md#Audit Settings|Audit ]]and [[windows-local-privilege-escalation/README.md#Wef|WEF ]]settings
- [ ] Check [[windows-local-privilege-escalation/README.md#Laps|LAPS]]
- [ ] Check if [[windows-local-privilege-escalation/README.md#Wdigest|WDigest ]]is active
- [ ] [[windows-local-privilege-escalation/README.md#Lsa Protection|LSA Protection]]?
- [ ] [[windows-local-privilege-escalation/README.md#Credentials Guard|Credentials Guard]][[windows-local-privilege-escalation/README.md#Cached Credentials|?]]
- [ ] [[windows-local-privilege-escalation/README.md#Cached Credentials|Cached Credentials]]?
- [ ] Check if any [[https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/windows-av-bypass/README.md|**AV**]]
- [ ] [[https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/authentication-credentials-uac-and-efs/README.md#applocker-policy|**AppLocker Policy**]]?
- [ ] [[https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/authentication-credentials-uac-and-efs/uac-user-account-control/README.md|**UAC**]]
- [ ] [[windows-local-privilege-escalation/README.md#Users And Groups|User Privileges]]
- [ ] Check [[windows-local-privilege-escalation/README.md#Users And Groups|current user privileges]]
- [ ] Are you [[windows-local-privilege-escalation/README.md#Privileged Groups|member of any privileged group]]?
- [ ] Check if you have [[windows-local-privilege-escalation/README.md#Token Manipulation|any of these tokens enabled]]: **SeImpersonatePrivilege, SeAssignPrimaryPrivilege, SeTcbPrivilege, SeBackupPrivilege, SeRestorePrivilege, SeCreateTokenPrivilege, SeLoadDriverPrivilege, SeTakeOwnershipPrivilege, SeDebugPrivilege** ?
- [ ] [[windows-local-privilege-escalation/README.md#Logged Users Sessions|Users Sessions]]?
- [ ] Check[[windows-local-privilege-escalation/README.md#Home Folders| users homes]] (access?)
- [ ] Check [[windows-local-privilege-escalation/README.md#Password Policy|Password Policy]]
- [ ] What is[[windows-local-privilege-escalation/README.md#Get The Content Of The Clipboard| inside the Clipboard]]?

### [[windows-local-privilege-escalation/README.md#Network|Network]]

- [ ] Check **current** [[windows-local-privilege-escalation/README.md#Network|network information]]
- [ ] Check **hidden local services** restricted to the outside

### [[windows-local-privilege-escalation/README.md#Running Processes|Running Processes]]

- [ ] Processes binaries [[windows-local-privilege-escalation/README.md#File And Folder Permissions|file and folders permissions]]
- [ ] [[windows-local-privilege-escalation/README.md#Memory Password Mining|Memory Password mining]]
- [ ] [[windows-local-privilege-escalation/README.md#Insecure Gui Apps|Insecure GUI apps]]
- [ ] Steal credentials with **interesting processes** via `ProcDump.exe` ? (firefox, chrome, etc ...)

### [[windows-local-privilege-escalation/README.md#Services|Services]]

- [ ] [[windows-local-privilege-escalation/README.md#Permissions|Can you modify any service?]]
- [ ] [[windows-local-privilege-escalation/README.md#Modify Service Binary Path|Can you modify the binary that is executed by any service?]]
- [ ] [[windows-local-privilege-escalation/README.md#Services Registry Modify Permissions|Can you modify the registry of any service?]]
- [ ] [[windows-local-privilege-escalation/README.md#Unquoted Service Paths|Can you take advantage of any unquoted service binary path?]]

### [[windows-local-privilege-escalation/README.md#Applications|Applications]]

- [ ] **Write** [[windows-local-privilege-escalation/README.md#Write Permissions|permissions on installed applications]]
- [ ] [[windows-local-privilege-escalation/README.md#Run At Startup|Startup Applications]]
- [ ] **Vulnerable** [[windows-local-privilege-escalation/README.md#Drivers|Drivers]]

### [[windows-local-privilege-escalation/README.md#Path Dll Hijacking|DLL Hijacking]]

- [ ] Can you **write in any folder inside PATH**?
- [ ] Is there any known service binary that **tries to load any non-existant DLL**?
- [ ] Can you **write** in any **binaries folder**?

### [[windows-local-privilege-escalation/README.md#Network|Network]]

- [ ] Enumerate the network (shares, interfaces, routes, neighbours, ...)
- [ ] Take a special look at network services listening on localhost (127.0.0.1)

### [[windows-local-privilege-escalation/README.md#Windows Credentials|Windows Credentials]]

- [ ] [[windows-local-privilege-escalation/README.md#Winlogon Credentials|Winlogon ]]credentials
- [ ] [[windows-local-privilege-escalation/README.md#Credentials Manager Windows Vault|Windows Vault]] credentials that you could use?
- [ ] Interesting [[windows-local-privilege-escalation/README.md#Dpapi|DPAPI credentials]]?
- [ ] Passwords of saved [[windows-local-privilege-escalation/README.md#Wifi|Wifi networks]]?
- [ ] Interesting info in [[windows-local-privilege-escalation/README.md#Saved Rdp Connections|saved RDP Connections]]?
- [ ] Passwords in [[windows-local-privilege-escalation/README.md#Recently Run Commands|recently run commands]]?
- [ ] [[windows-local-privilege-escalation/README.md#Remote Desktop Credential Manager|Remote Desktop Credentials Manager]] passwords?
- [ ] [[windows-local-privilege-escalation/README.md#Appcmd Exe|AppCmd.exe exists]]? Credentials?
- [ ] [[windows-local-privilege-escalation/README.md#Scclient Sccm|SCClient.exe]]? DLL Side Loading?

### [[windows-local-privilege-escalation/README.md#Files And Registry Credentials|Files and Registry (Credentials)]]

- [ ] **Putty:** [[windows-local-privilege-escalation/README.md#Putty Creds|Creds]] **and** [[windows-local-privilege-escalation/README.md#Putty Ssh Host Keys|SSH host keys]]
- [ ] [[windows-local-privilege-escalation/README.md#Ssh Keys In Registry|SSH keys in registry]]?
- [ ] Passwords in [[windows-local-privilege-escalation/README.md#Unattended Files|unattended files]]?
- [ ] Any [[windows-local-privilege-escalation/README.md#Sam And System Backups|SAM & SYSTEM]] backup?
- [ ] [[windows-local-privilege-escalation/README.md#Cloud Credentials|Cloud credentials]]?
- [ ] [[windows-local-privilege-escalation/README.md#Mcafee Sitelist.Xml|McAfee SiteList.xml]] file?
- [ ] [[windows-local-privilege-escalation/README.md#Cached Gpp Pasword|Cached GPP Password]]?
- [ ] Password in [[windows-local-privilege-escalation/README.md#Iis Web Config|IIS Web config file]]?
- [ ] Interesting info in [[windows-local-privilege-escalation/README.md#Logs|web logs]]?
- [ ] Do you want to [[windows-local-privilege-escalation/README.md#Ask For Credentials|ask for credentials]] to the user?
- [ ] Interesting [[windows-local-privilege-escalation/README.md#Credentials In The Recyclebin|files inside the Recycle Bin]]?
- [ ] Other [[windows-local-privilege-escalation/README.md#Inside The Registry|registry containing credentials]]?
- [ ] Inside [[windows-local-privilege-escalation/README.md#Browsers History|Browser data]] (dbs, history, bookmarks, ...)?
- [ ] [[windows-local-privilege-escalation/README.md#Generic Password Search In Files And Registry|Generic password search]] in files and registry
- [ ] [[windows-local-privilege-escalation/README.md#Tools That Search For Passwords|Tools]] to automatically search for passwords

### [[windows-local-privilege-escalation/README.md#Leaked Handlers|Leaked Handlers]]

- [ ] Have you access to any handler of a process run by administrator?

### [[windows-local-privilege-escalation/README.md#Named Pipe Client Impersonation|Pipe Client Impersonation]]

- [ ] Check if you can abuse it



