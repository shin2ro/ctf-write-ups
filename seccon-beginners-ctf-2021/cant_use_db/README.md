# cant_use_db

## Write-up

balance, noodles, soup がそれぞれ別のファイルで管理されている。  
balanceの書き込み前に ~~謎の~~ sleep がある。  

```
    if balance >= 10000:
        noodles += 1
        open(f"./users/{user_id}/noodles.txt", "w").write(str(noodles))
        time.sleep(random.uniform(-0.2, 0.2) + 1.0)
        balance -= 10000
        open(f"./users/{user_id}/balance.txt", "w").write(str(balance))
```

balance の書き込みが終わる前に noodles と soup を買う。  
具体的には素早くクリックする。  

## Flag

`ctf4b{r4m3n_15_4n_3553n714l_d15h_f0r_h4ck1n6}`
