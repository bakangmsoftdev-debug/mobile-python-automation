import unittest
import os
from app import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        self.test_log = "test_health.log"
        self.monitor = SystemMonitor(log_file=self.test_log)

    def tearDown(self):
        # Clean up test artifact after running
        if os.path.exists(self.test_log):
            os.remove(self.test_log)

    def test_format_status_message(self):
        msg = self.monitor.format_status_message()
        self.assertIn("STATUS: OK", msg)
        self.assertIn("RAM Usage", msg)

    def test_log_status_writes_file(self):
        self.monitor.log_status()
        self.assertTrue(os.path.exists(self.test_log))

if __name__ == "__main__":
    unittest.main()
