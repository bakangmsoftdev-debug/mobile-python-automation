import sys
import os
import hashlib
platform_name = sys.platform

def run_diagnostics():
    print(f"[*] Platform: {platform_name}")
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

if __name__ == "__main__":
    print("=== SecDevOps System & Hash Checker ===")
    run_diagnostics()

    test_file = "payload.txt"
    with open(test_file, "w") as f:
        f.write("SecDevOps Automation Pipeline Test\n")

    check_file_integrity(test_file)
