import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque()
queue.append((n, 0))
visited = [False] * 100001

while len(queue) != 0:
    tmp = queue.popleft()
    cur, dep = tmp[0], tmp[1]
    visited[cur] = True

    if cur == k:
        print(dep)
        break

    for i in range(-1, 2):
        nxt = 2 * cur if i == 0 else cur + i
        if 0 <= nxt <= 100000 and not visited[nxt]:
            queue.append((nxt, dep + abs(i)))
