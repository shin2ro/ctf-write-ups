from collections import Counter


def factor(n: int) -> Counter:
    r = []
    x = n
    i = 2
    while i * i <= n:
        if x % i == 0:
            r.append(i)
            x /= i
            continue
        i += 1

    if x != 1:
        r.append(x)

    return Counter(r)


def _main():
    x = 408410100000
    flag = '_'.join([f'{k}_{v}' for (k, v) in factor(x).items()])
    print(f'nitic_ctf{{{flag}}}')


if __name__ == '__main__':
    _main()
