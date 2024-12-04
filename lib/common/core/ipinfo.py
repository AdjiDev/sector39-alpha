import urllib.request

def Ambatron():
    try:
        with urllib.request.urlopen('https://api.ipify.org') as adjio:
            ip = adjio.read().decode()
        return ip
    except urllib.error.URLError as e:
        return f"N/A"
