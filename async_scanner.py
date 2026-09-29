import asyncio
import socket
import time

async def check_port(host, port, open_ports):
    conn = asyncio.open_connection(host, port)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=1.0)
        open_ports.append(port)
        print(f"  [+] Port {port} OPEN")
        writer.close()
        await writer.wait_closed()
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        pass

async def scan_ports_async(host, ports):
    print(f"[*] Starting Async Scan on target: {host}")
    start_time = time.time()
    open_ports = []
    
    tasks = [check_port(host, port, open_ports) for port in ports]
    await asyncio.gather(*tasks)
    
    elapsed = time.time() - start_time
    print(f"[+] Scan completed in {elapsed:.3f} seconds.")
    print(f"[+] Open Ports Found: {open_ports}")
    return sorted(open_ports)

def run_async_scan(host, ports):
    return asyncio.run(scan_ports_async(host, ports))

if __name__ == "__main__":
    run_async_scan("127.0.0.1", [21, 22, 80, 443, 8080])
