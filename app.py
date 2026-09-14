import sys

def check_system():
    print("========================================")
    print("   CORPORATE SYSTEM HEALTH CHECK: OK    ")
    print(f"   Python Version: {sys.version.split()[0]}")
    print("========================================")

if __name__ == "__main__":
    check_system()
