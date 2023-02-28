import sys

n = int(sys.stdin.readline())
d = []

for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

dp = [[int(2e9) for _ in range(1 << n)] for _ in range(n)]  # workers * 111111...


def backtracking(cur_worker, jobs):
    if jobs == (1 << n) - 1:  # xxx = 0
        return 0

    if dp[cur_worker][jobs] != int(2e9):  # already min
        return dp[cur_worker][jobs]

    for i in range(n):
        if not jobs & 1 << i:
            dp[cur_worker][jobs] = min(dp[cur_worker][jobs],
                                       backtracking(cur_worker + 1, jobs | 1 << i) + d[cur_worker][i])
            # dp[0][000] = min of dp[1][001], dp[1][010], dp[1][100], 001 -> oox

    return dp[cur_worker][jobs]


backtracking(0, 0)

print(dp)
