# please_not_trace_me

> フラグを復号してくれるのは良いけど，表示してくれない!!

## Write-up

gdbを使うと処理が終了するようになっています。
Ghidraを使ってデコンパイルしてから、Pythonで実装しました。

`solver.py`は以下の処理を元に実装しています。
- `e_i$nit`
- `generate_key`
- `rc4` 

## Flag

`ctf4b{d1d_y0u_d3crypt_rc4?}`
