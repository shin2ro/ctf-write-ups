# braincheck

> このプログラムは入力されたフラグをチェックします。

## Write-up

フラグをチェックする処理がBrainfuckで実装されています。
入力したフラグが正しい場合は`Correct`、間違っている場合は`Wrong`と出力されます。

`Wrong`を出力している処理を調べます。

```
[[-]>+++++++++++++++++[<+++++>-]<++.>+++++[<+++++>-]<++.---.-.-------.>>>>-<<<<[-]]
```

データポインタが指す値が`0`の場合に`Wrong`が出力されないことがわかります。
ブレークポイントが挿入できる webbf <https://github.com/primenumber/webbf> を使って、`Wrong`を出力する処理の前にデータポインタがどのデータを指しているか調べます。
入力したフラグが正しい場合は0番目のデータの値が0になることがわかります。

次に入力に関する処理を調べて0番目のデータの値が0にならない場合を調査します。

```
,[>+>+<<-]>>[<<+>>-]<<[-<->]<>++++++++++++++++++++++++++++++++++++++++++++++++[<----->-]<--[<+>[-]]>>[<<+>>-]<
,[>+>+<<-]>>[<<+>>-]<<[-<->]<----[<+>[-]]>>[<<+>>-]<
```

1文字読み込んだ後は似たような処理になっています。
1つ前の文字から入力した文字とある数を引いた数が0にならない場合に、0番目のデータの値が加算されます。
ソースコードからある数を求めることで正しい入力を計算することができます。


## Flag

`nitic_ctf{esoteric?}`
