"""
Simple Log Monitoring IDS
Author: Fujishima
Description:
A beginner-friendly Intrusion Detection System (IDS)
that detects suspicious IP addresses based on access frequency.

This version is designed for safe GitHub publication.
"""

import re
from collections import Counter
from datetime import datetime


# ==============================
# Configuration Section
# ==============================

THRESHOLD = 5  # Number of accesses considered suspicious
LOG_FILE = "sample_access.log"  # Change to "logs/real_access.log" for production


# ==============================
# Core Functions
# ==============================

def extract_ips(log_lines):
    """
    Extract IPv4 addresses from log lines using regex.

    Args:
        log_lines (list): List of log entries as strings

    Returns:
        list: Extracted IP addresses
    """
    ip_pattern = r"\d+\.\d+\.\d+\.\d+"
    ips = []

    for line in log_lines:
        match = re.search(ip_pattern, line)
        if match:
            ips.append(match.group())

    return ips


def detect_suspicious_ips(ips):
    """
    Detect IP addresses exceeding the defined threshold.

    Args:
        ips (list): List of extracted IP addresses

    Returns:
        dict: Suspicious IPs with access counts
    """
    counter = Counter(ips)

    # Dictionary comprehension for clean filtering
    suspicious = {
        ip: count for ip, count in counter.items()
        if count >= THRESHOLD
    }

    return suspicious


def generate_report(suspicious_ips):
    """
    Generate a console-based security report.

    Args:
        suspicious_ips (dict): IPs flagged as suspicious
    """
    print("=== Simple IDS Security Report ===")
    print("Generated at:", datetime.now())
    print("----------------------------------")

    if not suspicious_ips:
        print("No suspicious activity detected.")
    else:
        for ip, count in suspicious_ips.items():
            print(f"⚠ Suspicious IP: {ip} | Access count: {count}")


# ==============================
# Main Execution
# ==============================

def main():
    """
    Main execution flow:
    1. Read log file
    2. Extract IP addresses
    3. Detect suspicious IPs
    4. Generate report
    """
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()

        ips = extract_ips(logs)
        suspicious_ips = detect_suspicious_ips(ips)
        generate_report(suspicious_ips)

    except FileNotFoundError:
        print(f"Error: Log file '{LOG_FILE}' not found.")


if __name__ == "__main__":
    main()