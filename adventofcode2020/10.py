import fileinput
adapters = [int(x) for x in fileinput.input()]
sad = sorted(adapters + [0, max(adapters) + 3])

diffs = [sad[i+1] - sad[i] for i in range(len(sad) - 1)]

dp = [0] * (max(sad)) + [1]
for i in reversed(sad[:-1]):
    dp[i] = dp[i+3] + dp[i+2] + dp[i+1]

print(diffs.count(1) * diffs.count(3), dp[0])
