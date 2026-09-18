import os
import sys
import logging

class SystemMonitor:
    def __init__(self, log_path=None):
        self.log_path = log_path or os.getenv("LOG_FILE_PATH", "system.log")
        self._configure_logger()

    def _configure_logger(self):
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="%(asctime)s - [%(levelname)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def log_event(self, message):
        try:
            logging.info(message)
            return True
        except Exception as e:
            sys.stderr.write(f"Logging failed: {e}\n")
            return False

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.log_event("Day 4 Sprint: Standard logging module integrated successfully.")
    print(f"[*] Event logged to {monitor.log_path}")

