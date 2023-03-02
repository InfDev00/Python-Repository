import sys

n = int(sys.stdin.readline())
w = []
for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(1 << n)] for _ in range(n)]


def backtracking(cur, visited):
    if visited == (1 << n) - 1:
        if w[cur][0] == 0:
            return int(2e9)
        return w[cur][0]

    if not dp[cur][visited]:
        dp[cur][visited] = int(2e9)
        for nxt in range(n):
            if not visited & 1 << nxt and w[cur][nxt]:
                dp[cur][visited] = min(dp[cur][visited], backtracking(nxt, visited | 1 << nxt) + w[cur][nxt])

    return dp[cur][visited]


backtracking(0, 1)

print(dp[0][1])

# 2098
