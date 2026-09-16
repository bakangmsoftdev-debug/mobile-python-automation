import unittest
import os
from app import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        self.test_log = "test_health.log"
        self.monitor = SystemMonitor(log_file=self.test_log)

    def tearDown(self):
        if os.path.exists(self.test_log):
            os.remove(self.test_log)
        if os.path.exists("env_test_health.log"):
            os.remove("env_test_health.log")

    def test_format_status_message(self):
        msg = self.monitor.format_status_message()
        self.assertIn("STATUS: OK", msg)
        self.assertIn("RAM Usage", msg)

    def test_log_status_writes_file(self):
        self.monitor.log_status()
        self.assertTrue(os.path.exists(self.test_log))

    def test_env_variable_configuration(self):
        # Set temporary environment variable
        os.environ["LOG_FILE_PATH"] = "env_test_health.log"
        env_monitor = SystemMonitor()
        self.assertEqual(env_monitor.log_file, "env_test_health.log")
        env_monitor.log_status()
        self.assertTrue(os.path.exists("env_test_health.log"))
        del os.environ["LOG_FILE_PATH"]

if __name__ == "__main__":
    unittest.main()
