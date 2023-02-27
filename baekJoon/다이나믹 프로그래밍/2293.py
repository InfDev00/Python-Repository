import sys

n, k = map(int, sys.stdin.readline().split())

coins = list()
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0] * (k + 1)

dp[0] = 1

for j in range(n):
    for i in range(k+1):
        if i-coins[j] < 0:
            continue
        dp[i] += dp[i - coins[j]]

print(dp[k])