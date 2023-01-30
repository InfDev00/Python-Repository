import sys
from collections import deque

n = int(sys.stdin.readline())

mv_x, mv_y = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
visited = list()
board_size = -1
des_x, des_y = -1, -1


def BFS(x, y):
    queue = deque()
    depth = deque()
    visited[x][y] = True
    queue.append((x, y))
    depth.append(0)

    while len(queue) != 0:
        cur = queue.popleft()
        cur_dep = depth.popleft()

        if cur[0] == des_x and cur[1] == des_y:
            return cur_dep

        for i in range(8):
            nxt_x, nxt_y = cur[0] + mv_x[i], cur[1] + mv_y[i]
            if 0 <= nxt_x < board_size and 0 <= nxt_y < board_size:
                if not visited[nxt_x][nxt_y]:
                    visited[nxt_x][nxt_y] = True
                    queue.append((nxt_x, nxt_y))
                    depth.append(cur_dep+1)


for _ in range(n):
    board_size = int(sys.stdin.readline())
    srt_x, srt_y = map(int, sys.stdin.readline().split())
    des_x, des_y = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]

    print(BFS(srt_x, srt_y))
