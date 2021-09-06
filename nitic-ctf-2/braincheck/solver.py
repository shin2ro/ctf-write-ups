def solve():
    flag = 'ni'

    with open('source.bf') as f:
        bf_code = f.readline()

    for statement in bf_code.split('<,')[1:-1]:
        x = 0
        if statement[27:29] == '<>':
            i = 0
            while statement[29 + i] == '+':
                i += 1

            j = 0
            while statement[29 + i + 11 + j] == '-':
                j += 1

            x = i * 5 + j
        else:
            j = 0
            while statement[28 + j] == '-':
                j += 1
            x = j

        flag += chr(((ord(flag[-1]) + 256) - x) % 256)

    return flag


if __name__ == '__main__':
    print(solve())
