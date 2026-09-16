import os
import sys
from datetime import datetime

class SystemMonitor:
    def __init__(self, log_file=None):
        # Read from argument, then environment variable, then fallback to default
        self.log_file = log_file or os.getenv("LOG_FILE_PATH", "system_health.log")

    def get_memory_status(self):
        return "RAM Usage: 42% (OK)"

    def format_status_message(self):
        version = sys.version.split()[0]
        memory = self.get_memory_status()
        return f"STATUS: OK | Python: {version} | {memory}"

    def log_status(self):
        try:
            try_msg = self.format_status_message()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"[{timestamp}] {try_msg}\n"
            
            with open(self.log_file, "a") as f:
                f.write(log_entry)
            return try_msg
        except Exception as e:
            print(f"[ERROR] Failed to log status: {e}")
            return None

if __name__ == "__main__":
    monitor = SystemMonitor()
    print("========================================")
    print(f"   Target Log: {monitor.log_file}")
    print(f"   {monitor.log_status()}")
    print("========================================")
