import base64
from Crypto.Util.number import long_to_bytes


def solve():
    with open('distfiles/output.txt') as f:
        key = eval(f.readline().strip()[6:])
        flag = eval(f.readline().strip()[7:])

    flag = flag ^ key
    flag = long_to_bytes(flag)
    flag = base64.b64decode(flag)
    return flag.decode()


if __name__ == '__main__':
    print(solve())

