import urllib.request
import urllib.error

def check_endpoints(base_url, wordlist):
    print(f"[*] Starting Directory Recon on: {base_url}")
    for word in wordlist:
        target = f"{base_url}/{word}"
        try:
            req = urllib.request.Request(target, headers={'User-Agent': 'Parrot-Recon-Agent/1.0'})
            response = urllib.request.urlopen(req)
            if response.status == 200:
                print(f"    [+] Found: {target} (Status: 200 OK)")
        except urllib.error.HTTPError as e:
            if e.code in [403, 404]:
                print(f"    [-] Endpoint {word}: Status {e.code}")
        except urllib.error.URLError:
            print(f"[-] Connection failed to {base_url}")
            break

if __name__ == "__main__":
    wordlist = ["admin", "login", "payload.txt", "secret"]
    check_endpoints("http://127.0.0.1:8080", wordlist)
