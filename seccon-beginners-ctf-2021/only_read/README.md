# only_read

## Write-up

入力したフラグが正しいかチェックしてるところを読む。  

```
    11e0:	0f b6 45 e0          	movzbl -0x20(%rbp),%eax
    11e4:	3c 63                	cmp    $0x63,%al
    11e6:	0f 85 da 00 00 00    	jne    12c6 <main+0x13d>
    11ec:	0f b6 45 e1          	movzbl -0x1f(%rbp),%eax
    11f0:	3c 74                	cmp    $0x74,%al
    11f2:	0f 85 ce 00 00 00    	jne    12c6 <main+0x13d>
    11f8:	0f b6 45 e2          	movzbl -0x1e(%rbp),%eax
    11fc:	3c 66                	cmp    $0x66,%al
    11fe:	0f 85 c2 00 00 00    	jne    12c6 <main+0x13d>
    1204:	0f b6 45 e3          	movzbl -0x1d(%rbp),%eax
    1208:	3c 34                	cmp    $0x34,%al
    120a:	0f 85 b6 00 00 00    	jne    12c6 <main+0x13d>
    1210:	0f b6 45 e4          	movzbl -0x1c(%rbp),%eax
    1214:	3c 62                	cmp    $0x62,%al
    1216:	0f 85 aa 00 00 00    	jne    12c6 <main+0x13d>
    121c:	0f b6 45 e5          	movzbl -0x1b(%rbp),%eax
    1220:	3c 7b                	cmp    $0x7b,%al
    1222:	0f 85 9e 00 00 00    	jne    12c6 <main+0x13d>
    1228:	0f b6 45 e6          	movzbl -0x1a(%rbp),%eax
    122c:	3c 63                	cmp    $0x63,%al
    122e:	0f 85 92 00 00 00    	jne    12c6 <main+0x13d>
    1234:	0f b6 45 e7          	movzbl -0x19(%rbp),%eax
    1238:	3c 30                	cmp    $0x30,%al
    123a:	0f 85 86 00 00 00    	jne    12c6 <main+0x13d>
    1240:	0f b6 45 e8          	movzbl -0x18(%rbp),%eax
    1244:	3c 6e                	cmp    $0x6e,%al
    1246:	75 7e                	jne    12c6 <main+0x13d>
    1248:	0f b6 45 e9          	movzbl -0x17(%rbp),%eax
    124c:	3c 35                	cmp    $0x35,%al
    124e:	75 76                	jne    12c6 <main+0x13d>
    1250:	0f b6 45 ea          	movzbl -0x16(%rbp),%eax
    1254:	3c 74                	cmp    $0x74,%al
    1256:	75 6e                	jne    12c6 <main+0x13d>
    1258:	0f b6 45 eb          	movzbl -0x15(%rbp),%eax
    125c:	3c 34                	cmp    $0x34,%al
    125e:	75 66                	jne    12c6 <main+0x13d>
    1260:	0f b6 45 ec          	movzbl -0x14(%rbp),%eax
    1264:	3c 6e                	cmp    $0x6e,%al
    1266:	75 5e                	jne    12c6 <main+0x13d>
    1268:	0f b6 45 ed          	movzbl -0x13(%rbp),%eax
    126c:	3c 74                	cmp    $0x74,%al
    126e:	75 56                	jne    12c6 <main+0x13d>
    1270:	0f b6 45 ee          	movzbl -0x12(%rbp),%eax
    1274:	3c 5f                	cmp    $0x5f,%al
    1276:	75 4e                	jne    12c6 <main+0x13d>
    1278:	0f b6 45 ef          	movzbl -0x11(%rbp),%eax
    127c:	3c 66                	cmp    $0x66,%al
    127e:	75 46                	jne    12c6 <main+0x13d>
    1280:	0f b6 45 f0          	movzbl -0x10(%rbp),%eax
    1284:	3c 30                	cmp    $0x30,%al
    1286:	75 3e                	jne    12c6 <main+0x13d>
    1288:	0f b6 45 f1          	movzbl -0xf(%rbp),%eax
    128c:	3c 6c                	cmp    $0x6c,%al
    128e:	75 36                	jne    12c6 <main+0x13d>
    1290:	0f b6 45 f2          	movzbl -0xe(%rbp),%eax
    1294:	3c 64                	cmp    $0x64,%al
    1296:	75 2e                	jne    12c6 <main+0x13d>
    1298:	0f b6 45 f3          	movzbl -0xd(%rbp),%eax
    129c:	3c 31                	cmp    $0x31,%al
    129e:	75 26                	jne    12c6 <main+0x13d>
    12a0:	0f b6 45 f4          	movzbl -0xc(%rbp),%eax
    12a4:	3c 6e                	cmp    $0x6e,%al
    12a6:	75 1e                	jne    12c6 <main+0x13d>
    12a8:	0f b6 45 f5          	movzbl -0xb(%rbp),%eax
    12ac:	3c 67                	cmp    $0x67,%al
    12ae:	75 16                	jne    12c6 <main+0x13d>
    12b0:	0f b6 45 f6          	movzbl -0xa(%rbp),%eax
    12b4:	3c 7d                	cmp    $0x7d,%al
    12b6:	75 0e                	jne    12c6 <main+0x13d>
```

## Flag

`ctf4b{c0n5t4nt_f0ld1ng}`
