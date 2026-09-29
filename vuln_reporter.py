import json
import os
from datetime import datetime

# ANSI Color Codes for Termux Console Output
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

def analyze_vulnerabilities(target, open_ports, banner_info=None):
    findings = []
    
    for port in open_ports:
        if port == 21:
            findings.append({"port": 21, "severity": "HIGH", "issue": "FTP Plaintext Authentication Enabled"})
        elif port == 80:
            findings.append({"port": 80, "severity": "MEDIUM", "issue": "Unencrypted HTTP Service Operational"})
        elif port == 8080:
            findings.append({"port": 8080, "severity": "LOW", "issue": "Alternative HTTP Service Exposed"})

    if banner_info and "Python/3.13" in banner_info:
        findings.append({"port": "HTTP", "severity": "INFO", "issue": "Python Development Server Detected"})

    # Formatted Terminal UI Table Output
    print(f"\n{BLUE}+-------------------------------------------------------------------------+{RESET}")
    print(f"{BLUE}|              VULNERABILITY ASSESSMENT RESULTS - {target:<15} |{RESET}")
    print(f"{BLUE}+---------+----------+----------------------------------------------------+{RESET}")
    print(f"{BLUE}| PORT    | SEVERITY | ISSUE DESCRIPTION                                  |{RESET}")
    print(f"{BLUE}+---------+----------+----------------------------------------------------+{RESET}")

    for item in findings:
        sev = item["severity"]
        color = RED if sev == "HIGH" else (YELLOW if sev == "MEDIUM" else (GREEN if sev == "LOW" else BLUE))
        formatted_sev = f"{color}{sev:<8}{RESET}"
        port_str = f"{item['port']:<7}"
        issue_str = f"{item['issue']:<50}"
        print(f"| {port_str} | {formatted_sev} | {issue_str} |")

    print(f"{BLUE}+---------+----------+----------------------------------------------------+{RESET}")

    report_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "target": target,
        "open_ports": open_ports,
        "total_findings": len(findings),
        "findings": findings
    }

    report_filename = f"report_{target.replace('.', '_')}.json"
    with open(report_filename, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"[+] Report generated: {report_filename}")
    return report_filename

if __name__ == "__main__":
    analyze_vulnerabilities("127.0.0.1", [21, 80, 8080], banner_info="Python/3.13.5")
