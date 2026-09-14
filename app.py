import sys
from datetime import datetime

def get_memory_status():
    # Simulated memory status for local dev
    return "RAM Usage: 42% (OK)"

def check_system():
    try:
        mem_info = get_memory_status()
        status_msg = f"STATUS: OK | Python: {sys.version.split()[0]} | {mem_info}"
        
        print("========================================")
        print(f"   {status_msg}")
        print("========================================")
        
        with open("system_health.log", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {status_msg}\n")
            
    except Exception as e:
        print(f"[ERROR] Failed to execute system check: {e}")

if __name__ == "__main__":
    check_system()
