import requests

ProxyUrl = [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/socks4.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/socks5.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/refs/heads/master/proxy-list-raw.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
]

def CekProksi(proxy_url):
    try:
        SiAdji = requests.get(proxy_url, timeout=1)
        if SiAdji.status_code == 200:
            return SiAdji.text.splitlines()
        else:
            print(f"URL {proxy_url} tidak memberikan status 200.")
            return []
    except requests.RequestException as e:
        print(f"Terjadi kesalahan saat mengakses {proxy_url}: {e}")
        return []

def Caulila():
    Gelandangan = []
    for url in ProxyUrl:
        print(f"Mengambil proxy dari {url}...")
        proxies = CekProksi(url)
        if proxies:
            Gelandangan.extend(proxies)
    
    return Gelandangan

Gelandangan = Caulila()
print(f"\nProxy yang berhasil ditemukan:\n")

with open('proxy.txt', 'a') as fs:
    for proxy in Gelandangan:
        fs.write(proxy + '\n')
    print("Proxy {total_proxies} updated")
