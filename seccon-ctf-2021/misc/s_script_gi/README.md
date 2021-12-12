# s/<script>//gi

> Can you figure out why s/<script>//gi is insufficient for sanitizing? This can be bypassed with <scr<script>ipt>.
> Remove <script> (case insensitive) from the input until the input contains no <script>.

## Write-up

↓のような処理を実装しました。
- `<` の時にスタックにそれまでの文字列の開始と終了の位置を積む
- `>` の時に `<script>` となる場合はスタックから取り除く


## Flag

`SECCON{sanitizing_is_not_so_good><_escaping_is_better_iPt><SCript<ScrIpT<scRIp<scRI<Sc<scr!pt>}`

