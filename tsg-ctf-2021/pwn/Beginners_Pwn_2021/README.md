# Beginner's Pwn 2021

## Write-up

64文字入力すると`flag`の1文字目がNULL文字になります。
`'\x00' + 'a' * 63'`というペイロードを送ることで条件が`true`になり`win()`が実行されます。

## Flag

`TSGCTF{just_a_simple_off_by_one-chall_isnt_it}`
