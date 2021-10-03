# Kingtaker

## Write-up

`_y1._K2`にステージの情報があります。

```
[
    {_B1: "level1", width: 480, ...},
    {_B1: "level2", width: 480, ...},
    {_B1: "level3", width: 480, ...},
    {_B1: "level4", width: 480, ...},
    {_B1: "level5", width: 480, ...},
    {_B1: "ban", width: 480, ...},
]
```

`GameMaker_Init`が実行される前にlevel1からlevel4の情報を消します。

```js
_y1._K2.splice(0, 4)
```

## Flag

`CakeCTF{M4yb3_I_c4n_S3rv3_U_inst34d?}`
