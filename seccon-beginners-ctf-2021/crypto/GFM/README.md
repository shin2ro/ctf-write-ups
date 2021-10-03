# GFM

> - Github Flavored Markdown
> - Google Facebook Microsoft
> - And...?

## Write-up

与えられたpを使って`MatrixSpace`を生成します。
keyの逆行列とencを使ってMを求めることができます。

```
M = key_ms.inverse() * enc_ms * key_ms.inverse()
```

## Flag

`ctf4b{d1d_y0u_pl4y_w1th_m4tr1x_4nd_g4l0is_f1eld?}`
