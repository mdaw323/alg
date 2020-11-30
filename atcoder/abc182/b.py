n = int(input())
a = [int(x) for x in input().strip().split()]

res = a[0]
res_v = 1
for k in range(2, 1001):
    gcd = 0
    for ak in a:
        if ak % k == 0:
            gcd += 1
    if gcd > res_v:
        res_v = gcd
        res = k

print(res)
