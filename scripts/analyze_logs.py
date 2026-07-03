#!/usr/bin/env python3

import re
import csv
import json
from pathlib import Path
from collections import Counter
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# ============================================================
# Configuration
# ============================================================

LOG_FILE = Path("logs/alerts.log")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


# ============================================================
# Analyzer
# ============================================================

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

    analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ============================================================
    # TXT REPORT
    # ============================================================

    with open(REPORT_DIR / "report.txt", "w") as txt:

        txt.write("CodeAlpha IDS Detection Report\n")
        txt.write("=" * 50 + "\n\n")

        txt.write(f"Generated     : {analysis_time}\n")
        txt.write(f"Log File      : {LOG_FILE}\n")
        txt.write(f"Total Alerts  : {total_alerts}\n\n")

        txt.write("Alert Summary\n")
        txt.write("-" * 30 + "\n")

        for k, v in alerts.items():
            txt.write(f"{k:<15}: {v}\n")

        txt.write("\nTop Source IPs\n")
        txt.write("-" * 30 + "\n")

        for ip, count in src_ips.most_common(5):
            txt.write(f"{ip:<20}{count}\n")

        txt.write("\nTop Destination IPs\n")
        txt.write("-" * 30 + "\n")

        for ip, count in dst_ips.most_common(5):
            txt.write(f"{ip:<20}{count}\n")

    # ============================================================
    # CSV REPORT
    # ============================================================

    with open(REPORT_DIR / "report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Alert Type", "Count"])

        for k, v in alerts.items():
            writer.writerow([k, v])

    # ============================================================
    # JSON REPORT
    # ============================================================

    with open(REPORT_DIR / "report.json", "w") as jsonfile:

        json.dump(
            {
                "generated": analysis_time,
                "log_file": str(LOG_FILE),
                "total_alerts": total_alerts,
                "alert_summary": dict(alerts),
                "top_source_ips": dict(src_ips),
                "top_destination_ips": dict(dst_ips),
            },
            jsonfile,
            indent=4,
        )

    # ============================================================
    # DASHBOARD
    # ============================================================

    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + " CodeAlpha - Network Intrusion Detection System")
    print(Fore.CYAN + "=" * 60)

    print(Fore.GREEN + "\nDashboard & Alert Analysis")
    print("-" * 60)

    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + " CodeAlpha IDS Dashboard")
    print(Fore.CYAN + "=" * 60)

    print(f"\nAnalysis Time : {analysis_time}")
    print(f"Log File      : {LOG_FILE}")
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

    print("\nGenerated Reports")
    print("-" * 60)

    print(Fore.GREEN + "✓ report.txt")
    print(Fore.GREEN + "✓ report.csv")
    print(Fore.GREEN + "✓ report.json")

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + "Dashboard Complete")
    print(Fore.CYAN + "=" * 60)


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    analyze()
