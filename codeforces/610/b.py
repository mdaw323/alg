import sys

def ints():
    return map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    n, p, k = ints()
    A = list(sorted(ints()))
    dp = [0] * (n+1)    
    r = 0
    for i in range(1, n+1):
        dp[i] = A[i-1] + dp[i-1] if i < k else A[i-1] + dp[i-k]
        if dp[i] <= p:
            r = i
    print(r)
