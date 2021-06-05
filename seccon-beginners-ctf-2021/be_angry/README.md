# be_angry

> 読みづらいからって怒らないでください😢

## Write-up

正しいフラグを入力すると`Correct!!`と出力されます。
`Correct!!`を出力している処理に到達する入力をangrを使って探します。

```
    252d:	e9 0c 02 00 00       	jmpq   273e <main+0x15aa>
    2532:	48 8d 3d d7 0a 00 00 	lea    0xad7(%rip),%rdi        # 3010 <_IO_stdin_used+0x10>
    2539:	e8 32 eb ff ff       	callq  1070 <puts@plt>
```

## Flag

`ctf4b{3nc0d3_4r1thm3t1c}`
