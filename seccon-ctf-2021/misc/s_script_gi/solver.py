def solve(s):
    stack = []
    l = 0
    r = 0
    while r < len(s):
        if s[r] == '<':
            if l != r:
                stack.append((l, r))
            l = r
            r = l + 1
            continue
        if s[r] == '>':
            if s[l] == '<':
                if s[l:r + 1].lower() != '<script>':
                    stack.append((l, r + 1))
            else:
                t = ''
                j = 1
                while j <= len(stack):
                    tl, tr = stack[-j]
                    t = s[tl:tr] + t
                    if t[0] == '<':
                        break
                    j += 1
                t = t + s[l:r + 1]
                if t.lower() != '<script>':
                    stack.append((l, r + 1))
                else:
                    for _ in range(j):
                        stack.pop()
            l = r + 1
            r = l
            continue
        r += 1
    stack.append((l, r))

    return ''.join([s[l:r] for (l, r) in stack])


if __name__ == '__main__':
    filepath = './flag.txt'
    with open(filepath) as f:
        print(solve(f.readline()))

