import requests


if __name__ == '__main__':
    data = {
        'name': 'a',
        'color': 'red',
        '_Player__role': 'WEREWOLF'
    }
    r = requests.post("https://werewolf.quals.beginners.seccon.jp/", data=data)
    body = r.content.decode()
    print(body)
