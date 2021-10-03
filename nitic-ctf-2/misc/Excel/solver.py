from zipfile import ZipFile


def solve():
    flag = b''
    with ZipFile('./Book1.xlsx') as excel:
        for name in excel.namelist():
            with excel.open(name) as f:
                line = f.readline()
                i = line.find(b'nitic_ctf')
                if i >= 0:
                    flag = line[i:]
                    flag = flag[:flag.find(b'}') + 1]
    return flag.decode()


if __name__ == '__main__':
    print(solve())
