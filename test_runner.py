import unittest
import os
import sys_checker
import log_analyzer
import vuln_reporter

class TestSecDevOpsSuite(unittest.TestCase):

    def test_file_hash_computation(self):
        """Verify that SHA-256 hash generation produces a valid string."""
        h = sys_checker.get_file_hash("main.py")
        self.assertIsNotNone(h)
        self.assertEqual(len(h), 64)

    def test_vulnerability_report_generation(self):
        """Verify JSON report generation logic."""
        report = vuln_reporter.analyze_vulnerabilities("127.0.0.1", [21, 80], banner_info="Python/3.13")
        self.assertTrue(os.path.exists(report))

def run_pipeline_tests():
    print("==================================================")
    print("      CI/CD AUTOMATED PIPELINE SIMULATION         ")
    print("==================================================")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSecDevOpsSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n[+] CI/CD PIPELINE STATUS: PASSED (Ready for Release)")
        return True
    else:
        print("\n[-] CI/CD PIPELINE STATUS: FAILED")
        return False

if __name__ == "__main__":
    run_pipeline_tests()
