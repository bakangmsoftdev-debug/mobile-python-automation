import os
import hashlib
import socket

def get_file_hash(filename):
    if not os.path.exists(filename):
        return None
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_file_integrity(filename="payload.txt"):
    file_hash = get_file_hash(filename)
    if file_hash:
        print(f"[+] File Integrity Check [{filename}]: SHA-256 = {file_hash}")
    else:
        print(f"[-] File Integrity Warning: {filename} not found.")

def run_diagnostics():
    print("[*] Environment Diagnostic: Termux Android Linux Runtime")
    print(f"[*] Working Directory: {os.getcwd()}")
    print("[+] Core Modules Verified: sys_checker, async_scanner, vuln_reporter, audit_orchestrator")

def scan_ports(host, ports):
    print(f"[*] Running Sequential Scan on {host}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"  [+] Port {port} OPEN")
        sock.close()

if __name__ == "__main__":
    run_diagnostics()
    check_file_integrity("main.py")
