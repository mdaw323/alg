n = int(input())
for _ in range(n):
    d = [int(x) for x in input().strip().split()]
    m = max(d)
    s = sum(d)
    z = s - m
    if z > m:
        print(s//2)
    else:
        print(z)