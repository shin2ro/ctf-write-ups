from Crypto.Util.number import bytes_to_long, long_to_bytes


with open('output.txt') as f:
    N = eval(f.readline().strip()[4:])
    e = eval(f.readline().strip()[4:])
    c = eval(f.readline().strip()[4:])

m = bytes_to_long(b"the magic words are squeamish ossifrage. nitic_ctf{")
m = m << (8 * 8)

PR.<x> = PolynomialRing(Zmod(N))
f = (m + x) ^ e - c

print(long_to_bytes(m + f.small_roots(X=2^64, beta=1)[0]))
