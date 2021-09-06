alphabets = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
after1 = "fl38ztrx6q027k9e5su}dwp{o_bynhm14aicjgv"
after2 = "rho5b3k17pi_eytm2f94ujxsdvgcwl{}a086znq"


def conv(s: str, table: str) -> str:
    return ''.join([alphabets[table.find(c)] for c in s])


def solve():
    with open('flag') as f:
        enc_flag = f.readline().strip()

    for i in range(1 << 10):
        flag = enc_flag
        for j in range(10):
            if (i >> j & 1) == 1:
                flag = conv(flag, after1)
            else:
                flag = conv(flag, after2)

        if flag[:10] == 'nitic_ctf{':
            return flag


if __name__ == '__main__':
    print(solve())
