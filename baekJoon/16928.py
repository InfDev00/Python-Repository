import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ladders_and_snakes = dict()
for _ in range(n + m):
    s, d = map(int, sys.stdin.readline().split())
    ladders_and_snakes[s] = d

visited = [False for _ in range(101)]
queue = deque()
depth = deque()
queue.append(1)
depth.append(0)
while len(queue) != 0:
    cur = queue.popleft()
    cur_dep = depth.popleft()

    if cur == 100:
        print(cur_dep)
        break

    for i in range(1, 7):
        nxt = cur + i
        if nxt >= 100:
            queue.append(100)
            depth.append(cur_dep+1)
            break
        if nxt in ladders_and_snakes:
            if not visited[nxt] and not visited[ladders_and_snakes[nxt]]:
                visited[nxt], visited[ladders_and_snakes[nxt]] = True, True
                queue.append(ladders_and_snakes[nxt])
                depth.append(cur_dep + 1)
        else:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                depth.append(cur_dep+1)

# 16928
