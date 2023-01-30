import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
tower = list()
for _ in range(h):
    box = list()
    for _ in range(n):
        box.append(list(map(int, sys.stdin.readline().split())))
    tower.append(box)

mv_x, mv_y, mv_z = [1, 0, -1, 0, 0, 0], [0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 1, -1]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

x_lst, y_lst, z_lst, zeros = list(), list(), list(), 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tower[k][i][j] == 1:
                x_lst.append(j)
                y_lst.append(i)
                z_lst.append(k)
            elif tower[k][i][j] == 0:
                zeros += 1
            else:
                visited[k][i][j] = True

days = deque()
queue = deque()
for _ in range(len(x_lst)):
    x, y, z = x_lst.pop(), y_lst.pop(), z_lst.pop()
    visited[z][y][x] = True
    queue.append((x, y, z))
    days.append(0)

while len(queue) != 0:
    cur = queue.popleft()
    curday = days.popleft()
    if tower[cur[2]][cur[1]][cur[0]] == 0:
        zeros -= 1

    if zeros == 0:
        print(curday)
        break

    for i in range(6):
        nxt_x, nxt_y, nxt_z = cur[0] + mv_x[i], cur[1] + mv_y[i], cur[2] + mv_z[i]
        if 0 <= nxt_x < m and 0 <= nxt_y < n and 0 <= nxt_z < h:
            if not visited[nxt_z][nxt_y][nxt_x]:
                visited[nxt_z][nxt_y][nxt_x] = True
                queue.append((nxt_x, nxt_y, nxt_z))
                days.append(curday + 1)

if zeros != 0:
    print(-1)

# 7576
