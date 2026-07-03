# 🛡️ CodeAlpha - Network Intrusion Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Snort](https://img.shields.io/badge/Snort-3.12-red)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-success)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Passing-brightgreen)
![Version](https://img.shields.io/badge/Version-v1.0.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

A professional **Network Intrusion Detection System (NIDS)** developed using **Snort 3** and **Python** for detecting suspicious network activities in real time.

This project monitors live network traffic, applies **custom Snort detection rules**, captures security events, performs automated alert analysis, and generates professional reports in **TXT**, **CSV**, and **JSON** formats. It also provides a real-time dashboard that summarizes detected network events, top source and destination IP addresses, and alert statistics.

Developed as part of the **CodeAlpha Cyber Security Internship**, this project demonstrates practical knowledge of intrusion detection, rule development, packet inspection, log analysis, report generation, software testing, and continuous integration using **GitHub Actions**.

---

# 📑 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Custom Detection Rules](#-custom-detection-rules)
- [Live Packet Monitoring](#-live-packet-monitoring)
- [Dashboard & Alert Analysis](#-dashboard--alert-analysis)
- [Generated Reports](#-generated-reports)
- [Automated Testing](#-automated-testing)
- [Technologies Used](#technologies-used)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#author)

---

# 🚀 Features

| Feature | Status |
|----------|:------:|
| Snort 3 Integration | ✅ |
| Custom Detection Rules | ✅ |
| ICMP Detection | ✅ |
| HTTP Detection | ✅ |
| SSH Detection | ✅ |
| FTP Detection | ✅ |
| TCP SYN Scan Detection | ✅ |
| Live Packet Monitoring | ✅ |
| Alert Analysis Dashboard | ✅ |
| TXT Report Generation | ✅ |
| CSV Report Generation | ✅ |
| JSON Report Generation | ✅ |
| Professional CLI Output | ✅ |
| Automated Testing | ✅ |
| GitHub Actions CI | ✅ |
| MIT License | ✅ |

---

# 📸 Screenshots

The following screenshots demonstrate the implementation and functionality of the Network Intrusion Detection System.

---

## 1️⃣ Project Structure

Shows the complete project directory structure including Snort rules, reports, scripts, tests, GitHub Actions workflow, and supporting files.

![Project Structure](screenshots/01-project-structure.png)

---

## 2️⃣ Snort Version

Displays the installed Snort 3 version and runtime environment used for the project.

![Snort Version](screenshots/02-snort-version.png)

---

## 3️⃣ Custom Detection Rules

Shows the custom Snort detection rules implemented for identifying various network activities.

**Implemented Rules**

- ICMP Ping Detection
- HTTP Traffic Detection
- SSH Connection Detection
- FTP Connection Detection
- TCP SYN Scan Detection

![Custom Rules](screenshots/03-custom-rules.png)

---

## 4️⃣ ICMP Detection

Demonstrates successful detection of ICMP (Ping) traffic generated during live packet monitoring.

![ICMP Detection](screenshots/04-icmp-detection.png)

---

## 5️⃣ HTTP & TCP SYN Detection

Shows simultaneous detection of HTTP traffic and TCP SYN scan attempts using custom Snort rules.

![HTTP & TCP SYN Detection](screenshots/05-http-tcp-syn-detection.png)

---

## 6️⃣ Dashboard & Alert Analysis

Displays the automatically generated dashboard summarizing intrusion detection results, alert counts, and network statistics.

![Dashboard & Alert Analysis](screenshots/06-dashboard-analysis.png)

---

## 7️⃣ Generated Report

Illustrates the professionally generated detection report containing alert summaries, source/destination IPs, and analysis results.

![Generated Report](screenshots/07-generated-report.png)

---

## 8️⃣ GitHub Actions (CI/CD)

Demonstrates successful execution of automated testing through GitHub Actions Continuous Integration.

![GitHub Actions](screenshots/08-github-actions.png)

---

# 📂 Project Structure

The project follows a modular directory structure to separate Snort rules, analysis scripts, reports, automated tests, and documentation.

```text
CodeAlpha-Network-Intrusion-Detection-System/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── logs/
│   └── alerts.log
│
├── reports/
│   ├── assets/
│   ├── report.txt
│   ├── report.csv
│   ├── report.json
│   └── test_report.html
│
├── rules/
│   └── local.rules
│
├── screenshots/
│   ├── 01-project-structure.png
│   ├── 02-snort-version.png
│   ├── 03-custom-rules.png
│   ├── 04-icmp-detection.png
│   ├── 05-http-tcp-syn-detection.png
│   ├── 06-dashboard-analysis.png
│   ├── 07-generated-report.png
│   └── 08-github-actions.png
│
├── scripts/
│   └── analyze_logs.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_files.py
│   └── test_reports.py
│
├── CHANGELOG.md
├── LICENSE
├── README.md
├── VALIDATION.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/sahadatx/CodeAlpha-Network-Intrusion-Detection-System.git

cd CodeAlpha-Network-Intrusion-Detection-System
```

---

## Create a Virtual Environment

```bash
python3 -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## Verify Snort Installation

```bash
snort -V
```

Example

```text
Snort++ 3.12.2.0
Using DAQ version 3.0.24
Using libpcap version 1.10.6
Using OpenSSL 3.6.2
```

---

# 🚀 Usage

## Start Live Packet Monitoring

```bash
sudo snort \
-c /etc/snort/snort.lua \
-R rules/local.rules \
-i wlan0 \
-A alert_fast
```

Replace **wlan0** with your network interface if necessary.

---

## Generate Detection Reports

After collecting alerts, analyze the generated log file.

```bash
python3 scripts/analyze_logs.py
```

The script automatically creates

- report.txt
- report.csv
- report.json

inside the **reports/** directory.

---

# 🛡️ Custom Detection Rules

The IDS uses custom Snort rules to detect common network activities and potential security threats.

| Rule | Protocol | Port | Purpose |
|-------|----------|------|----------|
| ICMP Detection | ICMP | Any | Detects Ping Requests |
| HTTP Detection | TCP | 80 | Detects HTTP Connections |
| SSH Detection | TCP | 22 | Detects SSH Connections |
| FTP Detection | TCP | 21 | Detects FTP Connections |
| TCP SYN Detection | TCP | Any | Detects Possible SYN Scan |

---

## Example Rule

```snort
alert tcp any any -> any any (
    flags:S;
    msg:"[CodeAlpha] Possible TCP SYN Scan";
    sid:1000005;
    rev:1;
)
```

---

## Detection Workflow

```text
Incoming Network Traffic
            │
            ▼
      Snort Packet Capture
            │
            ▼
    Apply Custom Detection Rules
            │
            ▼
     Generate Security Alerts
            │
            ▼
      Save alerts.log
            │
            ▼
Python Log Analyzer
            │
            ▼
Generate Dashboard & Reports
```

---

# 📡 Live Packet Monitoring

The system continuously monitors live network traffic using **Snort 3** and applies custom detection rules in real time.

Whenever a rule matches incoming traffic, Snort immediately generates an alert that is stored in **logs/alerts.log** for further analysis.

Detected events include:

- ICMP Ping Requests
- HTTP Connections
- SSH Connections
- FTP Connections
- TCP SYN Scan Attempts

---

## Example Live Detection Output

```text
07/03-10:17:12
[CodeAlpha] Possible TCP SYN Scan

07/03-10:17:12
[CodeAlpha] HTTP Traffic Detected

07/03-10:17:25
[CodeAlpha] Possible TCP SYN Scan
```

---

## Monitoring Process

```text
Internet Traffic
        │
        ▼
 Network Interface (wlan0)
        │
        ▼
      Snort 3 Engine
        │
        ▼
 Custom Detection Rules
        │
        ▼
 Alert Generation
        │
        ▼
 logs/alerts.log
        │
        ▼
 Python Log Analyzer
        │
        ▼
 Dashboard & Reports
```

---

