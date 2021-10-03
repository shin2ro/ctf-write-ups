import pathlib
import string
import urllib.parse


def parse(export_dir: pathlib.Path):
    conditions = [[] for _ in range(50)]
    for path in export_dir.iterdir():
        if 'search_max=%28SELECT' in str(path):
            sql = str(path).split('search_max=')[1]
            sql = urllib.parse.unquote_plus(sql)

            i = int(sql.split(',')[1]) - 1
            mod = int(sql.split('%')[1])

            contents = path.open('r').read()
            remainder = contents.count('<th scope="row">')

            conditions[i].append((mod, remainder))
    return conditions


def conv(secret):
    letters = string.ascii_letters + string.digits + string.punctuation
    for letter in letters:
        for mod, r in secret:
            if ord(letter) % mod != r:
                break
        else:
            return letter

    return ''


def solve():
    export_dir = pathlib.Path('export')
    conditions = parse(export_dir)
    print(''.join([conv(condition) for condition in conditions]))


if __name__ == '__main__':
    solve()
