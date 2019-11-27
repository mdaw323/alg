def powr(p, x, s):
    # m = max(abs(p-x)-s, 0)
    # print("powr",p,x,s,m)
    return max(abs(p-x)-s, 0)


A = [(0, 0)]
inf = 9999
n, m = map(int, input().split())

for i in range(1, n+1):
    x, s = map(int, input().split())
    A.append((max(0, x-s), min(m, x+s)))
dp = [inf] * (m+1)
dp[0] = 0
A = sorted(A)

# for j in range(m+1):
#     dp[0][j] = 0
for p in range(1, m+1):

    for i in range(1, n+1):

        a, b = A[i]

        if p-1 >= a and p-1 <= b:
            dp[p] = dp[p-1]
        elif p > b:
            pwr = p-b +1
            dp[p] = min(dp[p], pwr + dp[p-pwr])


# for i in range(2, n+1):
#     x, s = A[i]
#     dp[i][1] = min(dp[i-1][1], powr(1, x, s))
#     for p in range(2, m+1):
#         dp[i][p] = max(dp[i][p-1], min(dp[i-1][p], powr(p, x, s)))


# print(A)
# for i in range(n+1):
    # print('\t'.join(str(dp[i][j]) for j in range(m+1)))

print(dp)
