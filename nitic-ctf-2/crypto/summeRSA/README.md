# summeRSA

> 彼も平文の一部がわかっていれば鼻血を出すまで解読を試みることはなかったかもしれません。

## Write-up

`task.py`を読むとに平文の一部がわかります。

```
m = bytes_to_long(b"the magic words are squeamish ossifrage. " + flag)
```

フラグのプレフィックスと連結することで、Coppersmith's Attackを利用できます。

> 平文mの上位ビットまたは下位ビットが知られてはいけない

<https://www.slideshare.net/sonickun/rsa-n-ssmjp#21>

## Flag

`nitic_ctf{k01k01!}`
