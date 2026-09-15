\# SentinelLoop Architecture



\## 5 Layers



1\. \*\*Attack Layer\*\* — Atomic Red Team + Caldera trigger MITRE techniques

2\. \*\*Telemetry Layer\*\* — Sysmon (host), Zeek/Suricata (network) capture events

3\. \*\*Detection Layer\*\* — Wazuh SIEM ingests logs, fires alerts via rules

4\. \*\*Backend (Brain)\*\* — FastAPI correlates attacks ↔ alerts, scores DDRS/DRI

5\. \*\*Frontend (Face)\*\* — React dashboard shows attack graph, scores, reports



\## Data Flow

Attack (T1059)

↓

Sysmon Event (Event ID 1)

↓

Wazuh Rule Match

↓

Alert in Wazuh DB

↓

Backend Correlation (attack time ↔ alert time window)

↓

DDRS Score + AI Report

↓

Dashboard





\## Key Endpoints



\- `POST /attacks` — Log a new attack

\- `GET /attacks/{id}/status` — Check if detected

\- `GET /ddrs` — Risk scores

