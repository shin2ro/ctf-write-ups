# Werewolf

## Write-up

ポストされた値を player に更新している処理があるので好きなロールに更新できる。  

```
        for k, v in request.form.items():
            player.__dict__[k] = v
```

プレフィックスがアンダースコア2つの変数は `_classname__variablename` という形式に置き換えられる。  

<https://docs.python.org/3/tutorial/classes.html#private-variables>

## Flag

`ctf4b{there_are_so_many_hackers_among_us}`
