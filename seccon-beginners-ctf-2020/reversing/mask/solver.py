if __name__ == '__main__':
    s1 = 'atd4`qdedtUpetepqeUdaaeUeaqau'
    s2 = 'c`b bk`kj`KbababcaKbacaKiacki'
    print(''.join([chr(ord(a) | ord(b)) for (a, b) in zip(s1, s2)]))
