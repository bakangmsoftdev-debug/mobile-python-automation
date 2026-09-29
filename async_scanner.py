import asyncio
import socket
import time

async def check_port(host, port, timeout=1.0):
    try:
        conn = asyncio.open_connection(host, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        print(f"    [+] Port {port:<5} OPEN")
        writer.close()
        await writer.wait_closed()
        return port, True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return port, False

async def scan_range(host, ports):
    print(f"[*] Starting Async Scan on target: {host}")
    start_time = time.time()
    
    tasks = [check_port(host, port) for port in ports]
    results = await asyncio.gather(*tasks)
    
    elapsed = time.time() - start_time
    open_ports = [port for port, is_open in results if is_open]
    print(f"[+] Scan completed in {elapsed:.3f} seconds.")
    print(f"[+] Open Ports Found: {open_ports if open_ports else 'None'}")

def run_async_scan(host, ports):
    asyncio.run(scan_range(host, ports))

if __name__ == "__main__":
    target_ports = [21, 22, 80, 443, 8080, 8443, 9000, 9999]
    run_async_scan("127.0.0.1", target_ports)
