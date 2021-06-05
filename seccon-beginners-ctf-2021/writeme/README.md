# writeme

> writeme.  
> (A little pwn)

## Write-up

競技終了後に [🔰 SECCON Beginners CTF 2021 作問者 Writeup](https://qiita.com/satoki/items/36837fce2fff7a584947#misc-writeme) を読んで解きました。

`42 >= 99`を`True`にすることでフラグを得ることができます。
任意のファイルの任意の位置に`Hack`と書き込む処理があるため、`/proc/self/mem`にある`42`のオブジェクトを書き換えることを考えます。

CPythonでは`id`を使うことでメモリ上のアドレスを調べることができます。
`writeme.py`には5文字のコードを実行して出力する処理があるため`id(1)`を使うことで`1`のアドレスを調べることができます。

> For CPython, `id(x)` is the memory address where `x` is stored.

<https://docs.python.org/3.9/reference/datamodel.html>

また、CPythonでは連続する小さい数値をキャッシュしているため`1`のアドレスから計算することができます。
`NSMALLNEGINTS + NSMALLPOSINTS` 個の連続する数値をキャッシュしています。

<https://github.com/python/cpython/blob/v3.9.2/Objects/longobject.c#L5754-L5794>

`42`のアドレスが分かったので次は`Hack`を書き込む位置を考えます。
Pythonの数値は`PyLongObject`という型で表現されています。

```
struct _longobject {
    PyObject_VAR_HEAD
    digit ob_digit[1];
};
```
<https://github.com/python/cpython/blob/v3.9.2/Include/longintrepr.h#L85-L88>

`ob_digit`に値があるので`42`の`ob_digit`(25バイト目)に`Hack`と書き込むことで`99`以上の数値になります。
