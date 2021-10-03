import requests


def solve():
    url = 'http://34.84.69.72:34705/'
    r = requests.post(url, json=None)
    content = r.content.decode()
    i = content.find('TSGCTF{')
    j = i + content[i:].find('}') + 1
    return content[i:j]


if __name__ == '__main__':
    print(solve())
