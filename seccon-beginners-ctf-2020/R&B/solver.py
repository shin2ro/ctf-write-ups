import base64
import codecs
import pathlib


def decode(s):
    if s[0] == 'B':
        return decode(base64.b64decode(s[1:]).decode())
    if s[0] == 'R':
        return decode(codecs.decode(s[1:], 'rot13'))
    return s


if __name__ == '__main__':
    file_path = pathlib.Path(__file__).parent / 'encoded_flag'
    with open(file_path) as f:
        print(decode(f.readline()))
