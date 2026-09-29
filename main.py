import argparse
import sys_checker
import parrot_banner
import parrot_dirscan
import log_analyzer

def main():
    parser = argparse.ArgumentParser(description="SecDevOps Mobile Toolset CLI")
    parser.add_argument("--diag", action="store_true", help="Run system diagnostics & payload hash check")
    parser.add_argument("--scan", type=str, metavar="HOST", help="Run multi-port scan on target host")
    parser.add_argument("--banner", nargs=2, metavar=("HOST", "PORT"), help="Grab service banner (e.g. --banner 127.0.0.1 8080)")
    parser.add_argument("--dirscan", type=str, metavar="URL", help="Run directory enumeration on target URL")
    parser.add_argument("--log", type=str, metavar="FILE", help="Analyze web server log file for security probes")

    args = parser.parse_args()

    if args.diag:
        print("=== Running Diagnostics ===")
        sys_checker.run_diagnostics()
        sys_checker.check_file_integrity("payload.txt")
    elif args.scan:
        print(f"=== Port Scan: {args.scan} ===")
        sys_checker.scan_ports(args.scan, [21, 22, 80, 443, 8080])
    elif args.banner:
        host, port = args.banner[0], int(args.banner[1])
        print(f"=== Banner Grab: {host}:{port} ===")
        parrot_banner.grab_banner(host, port)
    elif args.dirscan:
        print(f"=== Directory Recon: {args.dirscan} ===")
        wordlist = ["admin", "login", "payload.txt", "secret", "config"]
        parrot_dirscan.check_endpoints(args.dirscan, wordlist)
    elif args.log:
        print(f"=== Log Security Analysis ===")
        log_analyzer.parse_log(args.log)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
