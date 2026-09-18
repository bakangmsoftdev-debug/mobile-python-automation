import os

# Security Flaw 1: Hardcoded sensitive credentials
DB_PASSWORD = "SuperSecretAdminPassword123!"

def ping_host():
    # Security Flaw 2: Unsanitized user input passed directly to system shell
    user_input = input("Enter IP to ping: ")
    os.system(f"ping -c 1 {user_input}")

if __name__ == "__main__":
    ping_host()

