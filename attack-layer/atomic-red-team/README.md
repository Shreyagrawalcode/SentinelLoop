\# Atomic Red Team Integration



\## Setup



1\. \*\*Install on Windows VM:\*\*

```powershell

IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1')

```



2\. \*\*List available tests:\*\*

```powershell

Invoke-AtomicTest T1059.001 -ShowDetails

```



3\. \*\*Run a technique:\*\*

```powershell

Invoke-AtomicTest T1059.001 -Confirm:$false

```



\## Techniques to Test (Phase 2)



\- T1059.001 — PowerShell execution

\- T1003 — Credential dumping

\- T1021.002 — RDP lateral movement

\- T1078 — Valid accounts

\- T1482 — Domain trust discovery



See `/docs/TECHNIQUES.md` for full list.

