import sys

n, m, k = map(int, sys.stdin.readline().split())
board = list()
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip("\n")))

ans_board1 = [[0 for _ in range(m)] for _ in range(n)]
ans_board2 = [[0 for _ in range(m)] for _ in range(n)]

marker1 = ['B', 'W']
marker2 = ['W', 'B']


def board_sum1(y, x, c):
    ysum = ans_board1[y][x - 1] if 0 < x else 0
    xsum = ans_board1[y - 1][x] if 0 < y else 0
    xysub = ans_board1[y - 1][x - 1] if 0 < y and 0 < x else 0
    ans_board1[y][x] = ysum + xsum - xysub + c


def board_sum2(y, x, c):
    ysum = ans_board2[y][x - 1] if 0 < x else 0
    xsum = ans_board2[y - 1][x] if 0 < y else 0
    xysub = ans_board2[y - 1][x - 1] if 0 < y and 0 < x else 0
    ans_board2[y][x] = ysum + xsum - xysub + c


for i in range(n):
    for j in range(m):
        if board[i][j] != marker1[(i + j) % 2]:
            board_sum1(i, j, 1)
        else:
            board_sum1(i, j, 0)
        if board[i][j] != marker2[(i + j) % 2]:
            board_sum2(i, j, 1)
        else:
            board_sum2(i, j, 0)

ans1_list = list()
ans2_list = list()
for i in range(k - 1, n):
    for j in range(k - 1, m):
        xsub = ans_board1[i][j - k] if k <= j else 0
        ysub = ans_board1[i - k][j] if k <= i else 0
        xysum = ans_board1[i - k][j - k] if k <= j and k <= i else 0
        ans1_list.append(ans_board1[i][j] - xsub - ysub + xysum)
        xsub = ans_board2[i][j - k] if k <= j else 0
        ysub = ans_board2[i - k][j] if k <= i else 0
        xysum = ans_board2[i - k][j - k] if k <= j and k <= i else 0
        ans2_list.append(ans_board2[i][j] - xsub - ysub + xysum)

print(min(min(ans1_list), min(ans2_list)))
