n, k = [int(x) for x in input().strip().split()]
H = [int(x) for x in input().strip().split()]

dp = [0]+[10**9 + 7] * (n-1)
for i in range(n):
    for j in range(i+1, min(n, i+k+1)):
        dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))
print(dp[-1])
