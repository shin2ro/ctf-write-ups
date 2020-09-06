# just sqli

## Write-up

SELECT を入力するとエラーになるので VALUES を使って UNION する。  

<http://www.sqlite.org/draft/lang_select.html#values>

username に `' union values ('user', 1);` を入力する。  


## Flag

`KosenCTF{d0_y0u_kn0w_that_the_w0rd_va1u35_can_b3_aft3r_un10n}`
