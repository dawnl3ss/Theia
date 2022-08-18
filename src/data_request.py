from urllib.request import urlopen
import json

forbidden_keys = ["status", "query"]

def req_ip(ip):
    return json.loads(urlopen("http://ip-api.com/json/" + ip).read())