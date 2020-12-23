n = int(input())
H = [int(x) for x in input().strip().split()]

dp = [0] * n
dp[1] = abs(H[1] - H[0])
for i in range(2, n):
    dp[i] = min(
        dp[i-1] + abs(H[i] - H[i-1]),
        dp[i-2] + abs(H[i] - H[i-2]),
    )
print(dp[n-1])
