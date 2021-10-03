# Welcome to TSG CTF!

## Write-up

```
$ curl -XPOST http://34.84.69.72:34705/
{"statusCode":500,"error":"Internal Server Error","message":"Cannot read property 'TSGCTF{M4king_We6_ch4l1en9e_i5_1ik3_playing_Jenga}' of null"}
```

`app.js` を読みます。

```js
	if (typeof req.body === 'object' && req.body[flag] === true) {
		return res.send(`Nice! flag is ${flag}`);
	}
```

fastifyの`req.body`はリクエストのbodyが空の場合に`null`になるみたいです。
`typeof null`は`'object'`なので`typeof req.body === 'object'`が`true`となり`&&`の右側が評価されエラーが発生します。

## Flag

`TSGCTF{M4king_We6_ch4l1en9e_i5_1ik3_playing_Jenga}`
