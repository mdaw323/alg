N = int(input())
dp = []
dp.append([0] * N)
dp.append([0] * N)
dp.append([0] * N)
a, b, c = [int(x) for x in input().strip().split()]
dp[0][0] = a
dp[1][0] = b
dp[2][0] = c

for i in range(1, N):
    a, b, c = [int(x) for x in input().strip().split()]
    dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + a
    dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + b
    dp[2][i] = max(dp[1][i-1], dp[0][i-1]) + c

print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))
