# FILESTORE

> We stored our flag on this platform, but forgot to save the id. Can you help us restore it?

## Write-up

`filestore.py`の`store`の処理を読むと、以下のような処理が実装されていることがわかります。

- データをブロックに分割して保存
- 共通ブロックは再利用

共通ブロックを再利用しているため、以下の操作をすることで、すでに保存されているデータを特定することができます。

1. `status`を使って使用量を確認
2. `store`を使って16バイトのデータを保存
3. `status`を使って使用量を確認

`store`を使う前と後で使用量が変化していない場合は、保存したデータがすでに保存されていることがわかります。

フラグは`CTF{`から始まることがわかっているので、`CTF{`に文字を追加しながら保存されているフラグを特定します。


## Flag

`CTF{CR1M3_0f_d3dup1ic4ti0n}`
