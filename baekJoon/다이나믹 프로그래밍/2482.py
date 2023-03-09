import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

dp[1][1] = 1
for i in range(n + 1):
    dp[i][0] = 1

for i in range(2, n + 1):
    for j in range(1, k + 1):
        if i - 2 == 1 and j - 1 == 1:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1]

print(dp[n][k] % 1000000003)
