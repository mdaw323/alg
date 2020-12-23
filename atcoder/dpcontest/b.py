n, k = [int(x) for x in input().strip().split()]
H = [int(x) for x in input().strip().split()]

dp = [0]+[10**9 + 7] * (n-1)
for i in range(1, n):
    for j in range(1, k+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(H[i] - H[i-j]))
print(dp[n-1])
