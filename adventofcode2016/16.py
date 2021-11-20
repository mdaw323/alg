d = '01110110101001000'
l = 272
# l = 35651584

def solve(l):
    a = d
    while (len(a) < l):
        b = "".join(['1' if x == '0' else '0' for x in reversed(a)])
        a = a + '0' + b

    c = "".join(a[:l])
    while (len(c) % 2 == 0):
        c = "".join(['1' if c[2*i] == c[2*i+1] else '0' for i in range(len(c) // 2)])
    return c

print(solve(272), solve(35651584))
