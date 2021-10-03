import string


def solve():
    flag = ''.join([string.ascii_lowercase[ord(c) - ord('a') - 3] for c in 'fdhvdu'])
    return f'nitic_ctf{{{flag}}}'


if __name__ == '__main__':
    print(solve())
