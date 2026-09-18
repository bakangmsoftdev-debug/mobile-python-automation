import os
import subprocess
import ipaddress

# Remediation 1: Load sensitive values from environment variables
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_fallback_if_not_set")

def ping_host():
    user_input = input("Enter IP to ping: ").strip()
    
    # Remediation 2: Validate input format strictly
    try:
        ip_obj = ipaddress.ip_address(user_input)
    except ValueError:
        print("[!] Error: Invalid IP address format provided.")
        return

    # Remediation 3: Safe execution without shell invocation
    cmd = ["ping", "-c", "1", str(ip_obj)]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    ping_host()

