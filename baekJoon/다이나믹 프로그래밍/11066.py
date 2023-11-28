import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))

    dp = [[int(1e9)]*k for _ in range(k)]
    sum = [0]
    for r in range(k):
        for c in range(r,-1,-1):
            if r == c:
                dp[c][r] = 0
                sum.append(files[r]+sum[-1])
            else:
                for k in range(c, r):
                    dp[c][r] = min(dp[c][r],dp[c][k]+dp[k+1][r]+sum[r+1] - sum[c])
    print(dp[0][k+1])