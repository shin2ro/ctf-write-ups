# limited

## Write-up

PCAPファイルを開くとHTTPのパケットを確認できる。  
`search.php?keyword=&search_max=%28SELECT...` というリクエストを調べる。    

`search_max` に `select unicode(substr(secret, i, 1)) from account where name = 'admin') % mod` を指定している。  
(secret の i番目の文字を mod で割った数字を検索上限に指定している)  
レスポンスを見ることで検索結果の数がわかるのでi文字目をmodで割った余りを調べることができる。  

Wiresharkのオブジェクトをエクスポートを使って必要なパケットをエクスポートし「i文字目をmodで割った余り」を集めてフラグを復元する。  

> The flag format is KosenCTF{[\x21-\x7a]+} unless otherwise specified.

なので半角英数字と記号を総当たりしても時間はかからない。  


## Flag

`KosenCTF{u_c4n_us3_CRT_f0r_LIMIT_1nj3ct10n_p01nt}`
