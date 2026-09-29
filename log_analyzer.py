import re
from collections import Counter

def parse_log(file_path):
    print(f"[*] Analyzing Web Access Log: {file_path}")
    ip_counter = Counter()
    status_counter = Counter()
    failed_requests = []

    # Regex pattern matching standard HTTP access log format
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?"[A-Z]+\s+(.*?)\s+HTTP/.*?"\s+(\d{3})')

    try:
        with open(file_path, 'r') as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    ip, endpoint, status = match.groups()
                    ip_counter[ip] += 1
                    status_counter[status] += 1
                    
                    if status in ['403', '404']:
                        failed_requests.append((ip, endpoint, status))

        print("\n--- Summary Report ---")
        print(f"[+] Total Traffic Requests: {sum(ip_counter.values())}")
        print(f"[+] Status Breakdown: {dict(status_counter)}")
        
        if failed_requests:
            print("\n[!] Flagged Scanning Activity (403/404 Probes):")
            for ip, ep, st in failed_requests:
                print(f"    - IP: {ip} | Endpoint: {ep} | Status: {st}")
        else:
            print("[+] No suspicious scanning signatures detected.")

    except FileNotFoundError:
        print(f"[-] Error: Log file '{file_path}' not found.")

if __name__ == "__main__":
    parse_log("server.log")
