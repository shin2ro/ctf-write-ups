# MofuMofu Diary

## Write-up

Cookieにキャッシュしている画像の情報があります。
キャッシュの有効期限がきれた場合、Cookieの情報から画像を再度キャッシュしています。
`/flag.txt`の情報を持ったCookieを作成することでフラグを読み取ります。

```
cache = json.dumps({'data': [{'name': '/flag.txt', 'description': 'flag'}], 'expiry': 0})
```

## Flag

`CakeCTF{4n1m4ls_4r3_h0n3st_unl1k3_hum4ns_6e081a}`
