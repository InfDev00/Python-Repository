import sys

n, m, k = map(int, sys.stdin.readline().split())
board = list()
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip("\n")))

ans_board1 = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
ans_board2 = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

marker1 = ['B', 'W']
marker2 = ['W', 'B']

for i in range(n):
    for j in range(m):
        if board[i][j] != marker1[(i + j) % 2]:
            ans_board1[i + 1][j + 1] = ans_board1[i+1][j]+ans_board1[i][j+1]-ans_board1[i][j]+1
        else:
            ans_board1[i + 1][j + 1] = ans_board1[i+1][j]+ans_board1[i][j+1]-ans_board1[i][j]
        if board[i][j] != marker2[(i + j) % 2]:
            ans_board2[i + 1][j + 1] = ans_board2[i+1][j]+ans_board2[i][j+1]-ans_board2[i][j]+1
        else:
            ans_board2[i + 1][j + 1] = ans_board2[i+1][j]+ans_board2[i][j+1]-ans_board2[i][j]


ans1_list = list()
ans2_list = list()
for i in range(k, n + 1):
    for j in range(k, m + 1):
        ans1_list.append(ans_board1[i][j] - ans_board1[i - k][j]-ans_board1[i][j-k])
        ans2_list.append(ans_board2[i][j] - ans_board2[i - k][j]-ans_board2[i][j-k])

print(min(min(ans1_list), min(ans2_list)))
