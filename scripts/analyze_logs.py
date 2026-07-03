#!/usr/bin/env python3

import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path("logs/alerts.log")


def parse_logs():

    if not LOG_FILE.exists():
        print(f"[ERROR] {LOG_FILE} not found!")
        return

    total_alerts = 0

    alert_types = Counter()
    source_ips = Counter()
    destination_ips = Counter()

    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    with LOG_FILE.open("r", encoding="utf-8", errors="ignore") as logfile:

        for line in logfile:

            if "[**]" not in line:
                continue

            total_alerts += 1

            # Alert Types
            if "ICMP Ping Detected" in line:
                alert_types["ICMP"] += 1

            elif "HTTP Traffic Detected" in line:
                alert_types["HTTP"] += 1

            elif "SSH Connection Detected" in line:
                alert_types["SSH"] += 1

            elif "FTP Connection Detected" in line:
                alert_types["FTP"] += 1

            elif "Possible TCP SYN Scan" in line:
                alert_types["TCP SYN"] += 1

            # Extract IPs
            ips = ip_pattern.findall(line)

            if len(ips) >= 2:
                source_ips[ips[0]] += 1
                destination_ips[ips[1]] += 1

    print("=" * 50)
    print("      CodeAlpha IDS Log Analyzer")
    print("=" * 50)

    print(f"\nTotal Alerts : {total_alerts}\n")

    print("Alert Summary")
    print("-" * 50)

    for alert, count in alert_types.items():
        print(f"{alert:<15}: {count}")

    print("\nTop Source IPs")
    print("-" * 50)

    for ip, count in source_ips.most_common(5):
        print(f"{ip:<20}{count}")

    print("\nTop Destination IPs")
    print("-" * 50)

    for ip, count in destination_ips.most_common(5):
        print(f"{ip:<20}{count}")

    print("\nAnalysis Complete")


if __name__ == "__main__":
    parse_logs()
