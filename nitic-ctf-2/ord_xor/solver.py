def xor(c: str, n: int) -> str:
    """
    enc_sample.py
    """
    temp = ord(c)
    for _ in range(n):
        temp ^= n
    return chr(temp)


def solve():
    flag = ''
    with open('./flag') as f:
        for i, c in enumerate(f.readline().strip()):
            flag += xor(c, i)
    return flag


if __name__ == '__main__':
    print(solve())
