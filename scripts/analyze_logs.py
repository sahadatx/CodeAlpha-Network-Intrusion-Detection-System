#!/usr/bin/env python3

import re
import csv
import json
from pathlib import Path
from collections import Counter

LOG_FILE = Path("logs/alerts.log")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


def analyze():

    if not LOG_FILE.exists():
        print("Log file not found!")
        return

    total_alerts = 0

    alerts = Counter()
    src_ips = Counter()
    dst_ips = Counter()

    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:

        for line in file:

            if "[**]" not in line:
                continue

            total_alerts += 1

            if "ICMP Ping Detected" in line:
                alerts["ICMP"] += 1

            elif "HTTP Traffic Detected" in line:
                alerts["HTTP"] += 1

            elif "SSH Connection Detected" in line:
                alerts["SSH"] += 1

            elif "FTP Connection Detected" in line:
                alerts["FTP"] += 1

            elif "Possible TCP SYN Scan" in line:
                alerts["TCP SYN"] += 1

            ips = ip_pattern.findall(line)

            if len(ips) >= 2:
                src_ips[ips[0]] += 1
                dst_ips[ips[1]] += 1

    print("=" * 50)
    print(" CodeAlpha IDS Report Generator")
    print("=" * 50)

    print(f"\nTotal Alerts : {total_alerts}\n")

    print("Alert Summary")

    for k, v in alerts.items():
        print(f"{k:<15}: {v}")

    # ---------------- TXT ----------------

    with open(REPORT_DIR / "report.txt", "w") as txt:

        txt.write("CodeAlpha IDS Detection Report\n")
        txt.write("=" * 40 + "\n\n")

        txt.write(f"Total Alerts : {total_alerts}\n\n")

        txt.write("Alert Summary\n")

        for k, v in alerts.items():
            txt.write(f"{k}: {v}\n")

        txt.write("\nTop Source IPs\n")

        for ip, count in src_ips.most_common(5):
            txt.write(f"{ip} : {count}\n")

        txt.write("\nTop Destination IPs\n")

        for ip, count in dst_ips.most_common(5):
            txt.write(f"{ip} : {count}\n")

    # ---------------- CSV ----------------

    with open(REPORT_DIR / "report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Alert Type", "Count"])

        for k, v in alerts.items():
            writer.writerow([k, v])

    # ---------------- JSON ----------------

    data = {
        "total_alerts": total_alerts,
        "alert_summary": dict(alerts),
        "top_source_ips": dict(src_ips),
        "top_destination_ips": dict(dst_ips)
    }

    with open(REPORT_DIR / "report.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("\nReports Generated Successfully")
    print("reports/report.txt")
    print("reports/report.csv")
    print("reports/report.json")


if __name__ == "__main__":
    analyze()
