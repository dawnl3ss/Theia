from urllib.request import urlopen
import json


def version_check():
    return json.loads(urlopen("").read())