def decrypt(s: str) -> str:
    shift_table = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
    n = len(shift_table)
    while ord('0') <= ord(s[0]) <= ord('9'):
        shift = int(s[0])
        s = ''.join([shift_table[(shift_table.index(c) + n - shift) % n] for c in s[1:]])
    return s


def _main():
    encrypted_flag = '6}bceijnob9h9303h6yg896h0g896h0g896h01b40g896hz'
    flag = decrypt(encrypted_flag)
    print(flag)


if __name__ == '__main__':
    _main()
