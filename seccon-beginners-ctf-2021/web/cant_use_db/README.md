# cant_use_db

> Can't use DB.  
> I have so little money that I can't even buy the ingredients for ramen.  
> 🍜

## Write-up

`app.py`を読むと balance, noodles, soupがそれぞれ別のファイルで管理されていることがわかります。
`buy_noodles`や`buy_soup`の処理では、balanceの書き込み前に ~~謎の~~ `time.sleep`があります。

```
    if balance >= 10000:
        noodles += 1
        open(f"./users/{user_id}/noodles.txt", "w").write(str(noodles))
        time.sleep(random.uniform(-0.2, 0.2) + 1.0)
        balance -= 10000
        open(f"./users/{user_id}/balance.txt", "w").write(str(balance))
```

balanceの書き込みが終わる前にnoodlesとsoupを購入することで、noodleを2以上、soupを1以上購入することができます。
`time.sleep`の時間が長いので素早くクリックすることで購入することができます。

## Flag

`ctf4b{r4m3n_15_4n_3553n714l_d15h_f0r_h4ck1n6}`
