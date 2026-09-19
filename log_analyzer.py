import os
import re
from collections import Counter

# Target log files to inspect
LOG_FILES = ["system.log", "custom_app.log"]

# Suspicious patterns to flag
PATTERNS = {
    "Failed Login": r"(Failed password|Authentication failed|401 Unauthorized)",
    "Command Injection Attempt": r"(;|\|\||&&|`|\$\()",
    "Directory Traversal": r"(\.\./|\.\.\\)",
    "Resource Not Found (404)": r" 404 "
}

def analyze_logs():
    print("=== [SecDevOps] Automated Log Security Audit ===")
    
    for log_file in LOG_FILES:
        if not os.path.exists(log_file):
            print(f"[!] Warning: Log file '{log_file}' not found. Skipping.")
            continue
            
        print(f"\n[+] Analyzing: {log_file}")
        findings = Counter()
        
        with open(log_file, "r") as f:
            for line in f:
                for rule_name, pattern in PATTERNS.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        findings[rule_name] += 1
        
        if findings:
            for threat, count in findings.items():
                print(f"    - {threat}: {count} event(s) detected")
        else:
            print("    - No suspicious activity flagged.")

if __name__ == "__main__":
    analyze_logs()

