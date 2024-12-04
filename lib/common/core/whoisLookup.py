import urllib.request
import json

class LookupIp:
    def __init__(self, ip):
        self.ip = ip
        self.url = f'http://ipwho.is/{ip}'

    def _fuad(self):
        try:
            with urllib.request.urlopen(self.url) as fufufafa:
                data = fufufafa.read()
                return json.loads(data) 
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

    def type(self, keys=None):
        wanyad = self._fuad()  
        if wanyad:
            if keys:
                result = {key: wanyad.get(key, 'N/A') for key in keys}
                return ", ".join(f"{value}" for key, value in result.items())
            else:
                return wanyad.get("type", "N/A")
        return "N/A"

    def fullLookup(self):
        data = self._fuad()
        if data:
            return json.dumps(data, indent=4) 
        return "N/A"
