# Werewolf

> I wish I could play as a werewolf...

## Write-up

`app.py`を読むと`player.role`が`WEREWOLF`の時にフラグが表示されるようになっています。
しかし、`WEREWOLF`は選択されないようになっているので`WEREWOLF`を設定する方法を考えます。

ポストされた値を全てplayerに更新している処理があるので`WEREWOLF`を設定できそうです。

```
        for k, v in request.form.items():
            player.__dict__[k] = v
```

Pythonではプレフィックスがアンダースコア2つの変数は`_classname__variablename`という形式に置き換えられます。

<https://docs.python.org/3/tutorial/classes.html#private-variables>

`_Player__role=WEREWOLF`というデータをPOSTすることで`player.role`が`WEREWOLF`になりフラグが表示されます。

## Flag

`ctf4b{there_are_so_many_hackers_among_us}`
