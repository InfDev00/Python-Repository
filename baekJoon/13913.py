import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [-2 for _ in range(int(1e5)+1)]
queue = deque()
queue.append(n)
visited[n] = -1
while queue:
    cur = queue.popleft()
    if cur == k:
        break

    for nxt in [cur-1, cur+1, 2*cur]:
        if 0 <= nxt <= int(1e5) and visited[nxt] == -2:
            visited[nxt] = cur
            queue.append(nxt)

idx = k
ans = []
while idx != -1:
    ans.append(idx)
    idx = visited[idx]
ans.reverse()
print(len(ans)-1)
print(*ans)