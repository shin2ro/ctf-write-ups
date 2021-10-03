# Spy

## Write-up

DBにユーザーが存在する場合にパスワードのハッシュを計算している。  
ハッシュの計算ではソルトを追加してストレッチングをしているようなので、処理に時間がかかっているユーザーがDBに保存されているユーザーだとわかる。

app.pyのコメントがヒント。

> auth.calc_password_hash(salt, password) adds salt and performs stretching so many times.

## Flag

`ctf4b{4cc0un7_3num3r4710n_by_51d3_ch4nn3l_4774ck}`
