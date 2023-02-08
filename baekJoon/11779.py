import sys
from collections import deque

INF = int(2e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
route = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    route[a][b] = min(route[a][b], c)
s, d = map(int, sys.stdin.readline().split())

visited = [False for _ in range(n + 1)]
path = [0 for _ in range(n+1)]
cost = [INF for _ in range(n + 1)]
queue = deque([s])
cost[s] = 0

while queue:
    cur = queue.popleft()
    visited[cur] = True

    for i in range(n + 1):
        nxt = route[cur][i]
        if nxt != INF and cost[cur]+nxt < cost[i]:
            cost[i] = cost[cur] + nxt
            path[i] = cur

    nxt_idx = 0
    nxt = INF
    for i in range(n + 1):
        if not visited[i] and nxt > cost[i]:
            nxt = cost[i]
            nxt_idx = i
    queue.append(nxt_idx) if nxt_idx != 0 else 0

ans = []
idx = d
while idx != s:
    ans.append(idx)
    idx = path[idx]
ans.reverse()
print(cost[d])
print(len(ans)+1)
print(s, *ans)