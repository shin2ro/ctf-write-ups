import pathlib


if __name__ == '__main__':
    file_path = pathlib.Path(__file__).parent / 'emoemoencode.txt'
    with open(file_path, encoding='utf-8') as f:
        encoded = f.readline()[:-1]
        print(''.join([chr(ord(c) - 127744) for c in encoded]))
