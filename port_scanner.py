import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            return True
        return False
    except Exception:
        return False
    finally:
        s.close()

def main():
    target_host = "127.0.0.1"
    ports_to_scan = [22, 80, 443, 8022, 8080]

    print(f"[*] Starting TCP Port Scan on {target_host}...\n")
    
    for port in ports_to_scan:
        is_open = scan_port(target_host, port)
        state = "OPEN" if is_open else "CLOSED/FILTERED"
        print(f" Port {port}: {state}")

if __name__ == "__main__":
    main()


