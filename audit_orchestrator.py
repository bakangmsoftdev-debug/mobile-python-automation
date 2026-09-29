import async_scanner
import parrot_banner
import parrot_dirscan
import log_analyzer
import vuln_reporter
import os

def run_full_audit(target_host, target_url, log_file="sample.log"):
    print("==================================================")
    print(f"[*] STARTING FULL AUTOMATED AUDIT ON: {target_host}")
    print("==================================================")
    
    # 1. Async Port Scan
    print("\n--- PHASE 1: Asynchronous Port Scan ---")
    ports_to_check = [21, 22, 80, 443, 8080]
    open_ports = async_scanner.run_async_scan(target_host, ports_to_check)
    if open_ports is None:
        open_ports = []
    
    # 2. Service Banner Grabbing
    print("\n--- PHASE 2: Service Banner Grabbing ---")
    banner_info = ""
    if 8080 in open_ports:
        banner_info = parrot_banner.grab_banner(target_host, 8080)
    elif open_ports:
        banner_info = parrot_banner.grab_banner(target_host, open_ports[0])
    
    # 3. Directory Enumeration
    print("\n--- PHASE 3: Directory Enumeration ---")
    wordlist = ["admin", "login", "payload.txt", "secret", "config"]
    parrot_dirscan.check_endpoints(target_url, wordlist)
    
    # 4. Log File Security Analysis
    print("\n--- PHASE 4: Web Server Log Analysis ---")
    if log_file and os.path.exists(log_file):
        log_analyzer.parse_log(log_file)
    else:
        print(f"[-] Log file '{log_file}' not found. Skipping log analysis phase.")
    
    # 5. Vulnerability Report Synthesis
    print("\n--- PHASE 5: Report Synthesis ---")
    report_file = vuln_reporter.analyze_vulnerabilities(target_host, open_ports, banner_info=banner_info)
    
    print("\n==================================================")
    print(f"[+] AUDIT COMPLETE. Final Report: {report_file}")
    print("==================================================")

if __name__ == "__main__":
    run_full_audit("127.0.0.1", "http://127.0.0.1:8080")
