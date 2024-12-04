import socket
import urllib.request
import json

class warna:
    r = "\033[31m"
    g = "\033[32m"
    b = "\033[34m"
    y = "\033[33m"
    m = "\033[35m" 
    c = "\033[36m"
    bg_r = "\033[41m"
    bg_g = "\033[42m"
    bg_b = "\033[44m"
    bg_y = "\033[43m" 
    bg_m = "\033[45m"
    bg_c = "\033[46m"
    reset = "\033[0m"

class FindSubdomain:
    def __init__(self, target: str, file: str = "../src/subdo.txt"):
        self.target = target
        self.file = file
        self.results = []

    def SubdoToIp(self):
        try:
            with open(self.file, "r") as f:
                subdomains = f.read().splitlines()

            for sub in subdomains:
                subdomain = f"{sub}.{self.target}"
                try:
                    ip = socket.gethostbyname(subdomain)
                    self.results.append({"subdomain": subdomain, "ip": ip})
                except socket.gaierror:
                    self.results.append({"subdomain": subdomain, "ip": "Not Found"})
        except FileNotFoundError:
            print(f"Error: File {self.file} not found.")

    def WafCheck(self):
        for result in self.results:
            if result["ip"] == "Not Found":
                result["waf"] = "N/A"
                continue

            try:
                url = f"http://ip-api.com/json/{result['ip']}"
                with urllib.request.urlopen(url) as response:
                    if response.status == 200:
                        data = json.loads(response.read())
                        org = data.get("org", "Unknown").lower()

                        if "cloudflare" in org:
                            result["waf"] = "Cloudflare"
                        elif "incapsula" in org or "imperva" in org:
                            result["waf"] = "Incapsula"
                        elif "akamai" in org:
                            result["waf"] = "Akamai"
                        elif "f5" in org or "big-ip" in org:
                            result["waf"] = "F5"
                        elif "fortinet" in org:
                            result["waf"] = "Fortinet"
                        elif "sucuri" in org:
                            result["waf"] = "Sucuri"
                        else:
                            result["waf"] = "Unprotected"
                    else:
                        result["waf"] = "N/A"
            except urllib.error.URLError:
                result["waf"] = "Connection Error"

    def FetchResult(self):
        print(f"========================= {warna.g}SUBDOMAIN FINDER RESULT{warna.reset} =========================")
        for result in self.results:
            subdomain = result["subdomain"]
            ip = result["ip"]
            status = "Accessible" if ip != "Not Found" else "Not Accessible"
            waf = result.get("waf", "Unknown")

            print(f"{warna.y}URL{warna.reset}     : {subdomain}")
            print(f"{warna.y}IP{warna.reset}      : {ip}") 
            print(f"{warna.y}STATUS{warna.reset}  : {status}")
            print(f"{warna.y}WAF{warna.reset}     : {waf}")
            print("---------------------------------------------------------------------------")
