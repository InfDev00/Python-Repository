import sys

n = int(sys.stdin.readline())
costs = list()

for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().split())))


def get_min(srt_color):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0] = [costs[0][srt_color]] * 3

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + costs[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costs[i][2]
        if i == 1:
            dp[1][srt_color] = int(2e9)
        if i == n-1:
            dp[n-1][srt_color] = int(2e9)

    return min(dp[n - 1])


print(min(get_min(0), get_min(1), get_min(2)))