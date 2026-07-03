#!/usr/bin/env python3

import re
import csv
import json
from pathlib import Path
from collections import Counter
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

LOG_FILE = Path("logs/alerts.log")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


def analyze():

    if not LOG_FILE.exists():
        print(Fore.RED + "[ERROR] alerts.log not found!")
        return

    total_alerts = 0

    alerts = Counter()
    src_ips = Counter()
    dst_ips = Counter()

    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    with LOG_FILE.open("r", encoding="utf-8", errors="ignore") as file:

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

    # Generate Reports

    with open(REPORT_DIR / "report.txt", "w") as txt:

        txt.write("CodeAlpha IDS Detection Report\n")
        txt.write("=" * 40 + "\n\n")
        txt.write(f"Generated: {datetime.now()}\n\n")
        txt.write(f"Total Alerts: {total_alerts}\n\n")

        txt.write("Alert Summary\n")

        for k, v in alerts.items():
            txt.write(f"{k}: {v}\n")

    with open(REPORT_DIR / "report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Alert Type", "Count"])

        for k, v in alerts.items():
            writer.writerow([k, v])

    with open(REPORT_DIR / "report.json", "w") as jsonfile:

        json.dump({
            "generated": str(datetime.now()),
            "total_alerts": total_alerts,
            "alerts": dict(alerts),
            "top_source_ips": dict(src_ips),
            "top_destination_ips": dict(dst_ips)
        }, jsonfile, indent=4)

    # Dashboard

    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "        CodeAlpha Network IDS Dashboard")
    print(Fore.CYAN + "=" * 60)

    print(f"\nAnalysis Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Alerts  : {total_alerts}")

    print("\nAlert Summary")
    print("-" * 60)

    for name, count in alerts.items():
        print(f"{name:<15}: {count}")

    print("\nTop Source IPs")
    print("-" * 60)

    for ip, count in src_ips.most_common(5):
        print(f"{ip:<20}{count}")

    print("\nTop Destination IPs")
    print("-" * 60)

    for ip, count in dst_ips.most_common(5):
        print(f"{ip:<20}{count}")

    if alerts:
        top_alert = alerts.most_common(1)[0]

        print("\nMost Common Alert")
        print("-" * 60)
        print(f"{top_alert[0]} ({top_alert[1]} alerts)")

    print("\nReport Status")
    print("-" * 60)

    print(Fore.GREEN + "✓ report.txt")
    print(Fore.GREEN + "✓ report.csv")
    print(Fore.GREEN + "✓ report.json")

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + "Dashboard Complete")
    print(Fore.CYAN + "=" * 60)


if __name__ == "__main__":
    analyze()
