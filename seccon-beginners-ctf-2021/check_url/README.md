# check_url

## Write-up

指定したURLへアクセスしてインラインフレームで表示するサイト。  
URLのチェックが厳しい。  

```php
              $url = $_GET["url"];
              if ($url !== "https://www.example.com"){
                $url = preg_replace("/[^a-zA-Z0-9\/:]+/u", "👻", $url); //Super sanitizing
              }
              if(stripos($url,"localhost") !== false || stripos($url,"apache") !== false){
                die("do not hack me!");
              }
```

英数字のみでlocalhostを表現すれば突破できそうなので調べてみると  
[127.0.0.1(localhost)を一番面白く表記できた奴が優勝](https://qiita.com/naka_kyon/items/88478be20b300e757fc0)  
というちょうどよい記事があった。  

<https://check-url.quals.beginners.seccon.jp/?url=https://0x7F000001>

## Flag

`ctf4b{5555rf_15_53rv3r_51d3_5up3r_54n171z3d_r3qu357_f0r63ry}`
