# writeme

## Write-up

作問者のWrite-up

<https://qiita.com/satoki/items/36837fce2fff7a584947#misc-writeme>

Pythonは `NSMALLNEGINTS + NSMALLPOSINTS` 個の連続する数値をキャッシュしている。

<https://github.com/python/cpython/blob/v3.9.2/Objects/longobject.c#L5754-L5794>

PyLongObjectの構造
- 参照カウント
- `PyTypeObject` のポインタ
- 値の要素数
- 値

<https://github.com/python/cpython/blob/v3.9.2/Include/longintrepr.h#L85-L88>

`42` の値に `Hack` を書き込むことで `42 >= 99` が `True` になる。

```
    if 42 >= 99:
        print(open("flag").readline()) # Congrats!
    else:
        print(fd.readline())
```
