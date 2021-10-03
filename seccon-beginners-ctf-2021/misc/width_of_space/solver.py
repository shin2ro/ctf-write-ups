def solve():
    with open('problem.txt', encoding='utf-8') as f:
        s = f.readline()[:-1]

    flag = ''

    for i in range(0, len(s), 16):
        c = 0
        if s[i + 8] not in ('\u200b', '\u200c'):
            break

        for j in range(0, 8):
            c = c << 1
            c = c + (ord(s[i+8+j]) - 8203)

        flag += chr(c)

    return flag


if __name__ == '__main__':
    print(solve())
