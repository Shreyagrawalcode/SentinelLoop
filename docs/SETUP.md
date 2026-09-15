\# SentinelLoop Setup Guide



\## Hardware

\- 16 GB RAM: Windows 10 VM (4GB) + Ubuntu Server (2GB) + Kali (2GB)

\- Single laptop, run 1-2 VMs at a time



\## Lab VMs

1\. \*\*Windows 10\*\* — target for attacks, Sysmon logs

2\. \*\*Ubuntu Server\*\* — Wazuh manager, Zeek, Suricata

3\. \*\*Kali Linux\*\* — attacker machine (optional, use host if constrained)



\## Quick Start

```bash

docker-compose up

```



\- Wazuh: http://localhost:5601 (admin/SecretPassword)

\- API: http://localhost:8000/docs



\## Next Steps

1\. Install Sysmon on Windows VM

2\. Deploy Wazuh agent on Windows

3\. Ship logs to Wazuh manager

4\. Test with Atomic Red Team



See ROADMAP.md for phases.

