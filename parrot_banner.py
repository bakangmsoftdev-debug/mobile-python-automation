import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        
        # Send a basic HTTP request header when probing web ports
        if port in [80, 8080]:
            s.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            
        banner = s.recv(1024)
        print(f"[+] Banner from {ip}:{port}:\n{banner.decode('utf-8', errors='ignore').strip()}")
        s.close()
    except Exception as e:
        print(f"[-] Could not retrieve banner on port {port}: {e}")

if __name__ == "__main__":
    print("=== Security Lab: Banner Grabber ===")
    grab_banner("127.0.0.1", 8080)


