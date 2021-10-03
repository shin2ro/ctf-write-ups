# protected

> パスワードでフラグを保護すれば安全！

## Write-up

```
$ strings ./chall

PASSWORD:
sUp3r_s3Cr37_P4s5w0Rd
Invalid password.
```

パスワードぽい文字列があるので入力してみます。

```
$ ./chall
PASSWORD: sUp3r_s3Cr37_P4s5w0Rd
nitic_ctf{hardcode_secret}
```

## Flag

`nitic_ctf{hardcode_secret}`
