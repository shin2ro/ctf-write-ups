from pathlib import Path


def read_data(path: Path):
    with open(path, 'rb') as f:
        f.seek(0x23F)
        contents = f.read()
    return contents


def solve():
    data = read_data(Path('./harmagedon'))

    choices = ""

    i = 0xb77c7c
    for _ in range(11):
        i = i >> 2
        i -= 1
        choices += chr(data[i])

    print(f'KosenCTF{{{choices[::-1]}}}')


if __name__ == '__main__':
    solve()
