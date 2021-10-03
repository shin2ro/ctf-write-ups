# password

> パスワードの文字が紛らわしいので、打ち間違えても通るようにしました。

## Write-up

パスワードをチェックしている処理を調べます。

```
		else:
			c = input_pass[i]
		if all([ci != password[i] for ci in c]):
			return False
```

`password[i]`が`input_pass[i]`に1文字あればよいので`string.ascii_letters`の配列を投げます。

## Flag

`nitic_ctf{s0_sh0u1d_va11dat3_j50n_sch3m3}`
