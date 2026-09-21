import sys
import os
import hashlib
import socket

def run_diagnostics():
    print(f"[*] Platform: {sys.platform}")
    print(f"[*] Python Version: {sys.version.split()[0]}")

def check_file_integrity(filepath):
    if not os.path.exists(filepath):
        print(f"[-] Error: {filepath} not found.")
        return
    
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    print(f"[+] SHA-256 Hash of {filepath}: {sha256_hash.hexdigest()}")

def scan_ports(host, ports):
    print(f"\n[*] Scanning Target: {host}")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"    [+] Port {port}: OPEN")
        else:
            print(f"    [-] Port {port}: CLOSED")
        s.close()

if __name__ == "__main__":
    print("=== SecDevOps System & Network Checker ===")
    run_diagnostics()
    
    test_file = "payload.txt"
    check_file_integrity(test_file)
    
    # Scan common ports on local loopback
    target_ports = [21, 22, 80, 443, 8080]
    scan_ports("127.0.0.1", target_ports)
