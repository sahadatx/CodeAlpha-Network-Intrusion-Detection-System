# 🛡️ CodeAlpha - Network Intrusion Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Snort](https://img.shields.io/badge/Snort-3.12-red)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-success)
[![GitHub Actions](https://github.com/sahadatx/CodeAlpha-Network-Intrusion-Detection-System/actions/workflows/python-tests.yml/badge.svg)](https://github.com/sahadatx/CodeAlpha-Network-Intrusion-Detection-System/actions/workflows/python-tests.yml)
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

![Project Structure](screenshots/01-project-structure.png)

---

## 2️⃣ Snort Version

![Snort Version](screenshots/02-snort-version.png)

---

## 3️⃣ Custom Detection Rules

**Implemented Rules**

- ICMP Ping Detection
- HTTP Traffic Detection
- SSH Connection Detection
- FTP Connection Detection
- TCP SYN Scan Detection

![Custom Rules](screenshots/03-custom-rules.png)

---

## 4️⃣ ICMP Detection

![ICMP Detection](screenshots/04-icmp-detection.png)

---

## 5️⃣ HTTP & TCP SYN Detection

![HTTP & TCP SYN Detection](screenshots/05-http-tcp-syn-detection.png)

---

## 6️⃣ Dashboard & Alert Analysis

![Dashboard & Alert Analysis](screenshots/06-dashboard-analysis.png)

---

## 7️⃣ Generated Report

![Generated Report](screenshots/07-generated-report.png)

---

## 8️⃣ GitHub Actions (CI/CD)

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


# 📊 Dashboard & Alert Analysis

The Python log analyzer automatically processes **Snort alert logs** and generates a professional dashboard that summarizes the detected network events.

The dashboard provides a quick overview of intrusion attempts, alert statistics, and network activity.

---

## Dashboard Overview

The dashboard includes:

- Analysis Timestamp
- Log File Information
- Total Alerts Detected
- Alert Summary
- Top Source IP Addresses
- Top Destination IP Addresses
- Most Common Alert
- Generated Report Status

---

## Example Dashboard Output

```text
============================================================
CodeAlpha IDS Dashboard
============================================================

Total Alerts : 42

Alert Summary

TCP SYN : 3
HTTP    : 9
ICMP    : 30

Most Common Alert

ICMP (30 alerts)

```

---

# 📄 Generated Reports

After processing **logs/alerts.log**, the analyzer automatically generates reports in multiple formats for documentation and further analysis.

Generated Files

```text
reports/
├── report.txt
├── report.csv
└── report.json
```

---

## TXT Report

The TXT report provides a human-readable summary of the detected alerts.

It includes:

- Report Generation Time
- Log File Name
- Total Alerts
- Alert Summary
- Top Source IP Addresses
- Top Destination IP Addresses

---


# 🧪 Automated Testing

The project includes automated tests developed using **Pytest** to verify the functionality of the IDS log analyzer.

The test suite validates:

- Python Analyzer
- Report Generation
- Project Structure
- Detection Rules
- Generated Files

---

## Run Tests

```bash
python -m pytest -v
```

---

## Example Output

```text
============================= test session starts =============================

collected 7 items

tests/test_analyzer.py ........ PASSED
tests/test_files.py ........... PASSED
tests/test_reports.py ......... PASSED

==============================

7 passed in 0.04s

==============================
```

---


# 💻 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 3.13 | Programming Language |
| Snort 3 | Network Intrusion Detection |
| Kali Linux | Development Platform |
| Pytest | Automated Testing |
| GitHub Actions | Continuous Integration |
| Git | Version Control |
| GitHub | Source Code Hosting |
| CSV | Report Generation |
| JSON | Structured Data Export |
| Regular Expressions | Log Parsing |

---

# 🔮 Future Improvements

The following enhancements are planned for future releases:

- 📧 Email Alert Notifications
- 🌐 Web-based Dashboard
- 📊 Interactive Charts
- 🌍 Geo-IP Location Detection
- 🧠 Threat Intelligence Integration
- 📡 Multi-Interface Monitoring
- ☁️ Cloud Report Storage
- 🐳 Docker Deployment
- 📈 Real-Time Analytics
- 🔐 Advanced Detection Rules

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please ensure that:

- Code follows PEP 8 guidelines.
- New functionality includes appropriate tests.
- Documentation is updated whenever necessary.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software under the terms of the MIT License.

For more information, see the **LICENSE** file.

---

# 👨‍💻 Author

**Sahadat Hossain**

Cybersecurity Enthusiast

- 📧 Email: pentester.sahadathossain@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/pentester-sahadat-hossain/
- 🐙 GitHub: https://github.com/sahadatx

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share it with others

---

<div align="center">

Made with ❤️ by **Sahadat Hossain**

⭐ If you found this project helpful, please consider giving it a Star.

</div>