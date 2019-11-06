n,m = map(int, input().split())
p = (int)(1e9 + 7)
print(pow(pow(2, m, p)-1, n, p))