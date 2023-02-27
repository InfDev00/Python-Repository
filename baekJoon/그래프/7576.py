import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = list()
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))
mv_x, mv_y = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
ans = 0

x_lst, y_lst, zeros = list(), list(), 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            x_lst.append(j)
            y_lst.append(i)
        elif box[i][j] == 0:
            zeros += 1
        else:
            visited[i][j] = True

days = deque()
queue = deque()
for _ in range(len(x_lst)):
    x, y = x_lst.pop(), y_lst.pop()
    visited[y][x] = True
    queue.append((x, y))
    days.append(0)

while len(queue) != 0:
    cur = queue.popleft()
    curday = days.popleft()
    if box[cur[1]][cur[0]] == 0:
        zeros -= 1

    if zeros == 0:
        print(curday)
        break

    for i in range(4):
        nxt_x, nxt_y = cur[0] + mv_x[i], cur[1] + mv_y[i]
        if 0 <= nxt_x < m and 0 <= nxt_y < n:
            if not visited[nxt_y][nxt_x]:
                visited[nxt_y][nxt_x] = True
                queue.append((nxt_x, nxt_y))
                days.append(curday + 1)

if zeros != 0:
    print(-1)

# 7576
