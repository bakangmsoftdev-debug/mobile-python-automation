import json
import os
from datetime import datetime

def analyze_vulnerabilities(target, open_ports, banner_info=None):
    print(f"[*] Generating Vulnerability Report for Target: {target}")
    
    findings = []
    
    # Known risk checks
    for port in open_ports:
        if port == 21:
            findings.append({"port": 21, "severity": "HIGH", "issue": "FTP Plaintext Authentication Enabled"})
        elif port == 80:
            findings.append({"port": 80, "severity": "MEDIUM", "issue": "Unencrypted HTTP Service Operational"})
        elif port == 8080:
            findings.append({"port": 8080, "severity": "LOW", "issue": "Alternative HTTP Service Exposed"})

    if banner_info and "Python/3.13" in banner_info:
        findings.append({"port": "HTTP", "severity": "INFO", "issue": "Python Development Server Detected in Production"})

    report_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "target": target,
        "open_ports": open_ports,
        "total_findings": len(findings),
        "findings": findings
    }

    # Export to JSON format
    report_filename = f"report_{target.replace('.', '_')}.json"
    with open(report_filename, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"[+] Report generated successfully: {report_filename}")
    print(f"[+] Total Vulnerabilities/Flags Identified: {len(findings)}")
    return report_filename

if __name__ == "__main__":
    analyze_vulnerabilities("127.0.0.1", [21, 80, 8080], banner_info="Server: SimpleHTTP/0.6 Python/3.13.5")
