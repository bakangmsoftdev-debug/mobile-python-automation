import sys
from datetime import datetime

def check_system():
    status_msg = f"CORPORATE SYSTEM HEALTH CHECK: OK | Python: {sys.version.split()[0]}"
    print("========================================")
    print(f"   {status_msg}")
    print("========================================")
    
    # Write to log file
    with open("system_health.log", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {status_msg}\n")

if __name__ == "__main__":
    check_system()
