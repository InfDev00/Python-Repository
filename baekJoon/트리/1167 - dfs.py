import sys

INF = int(2e9)
v = int(sys.stdin.readline())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    node = tmp[0]
    idx = 1
    while tmp[idx] != -1:
        tree[node].append([tmp[idx], tmp[idx + 1]])
        idx += 2


def DFS(cur):
    for chd in tree[cur]:
        nxt, cost = chd[0], chd[1]
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + cost
            DFS(nxt)


ans = 0
idx = 1
for _ in range(2):
    visited = [-1 for _ in range(v + 1)]
    visited[idx] = 0
    DFS(idx)
    max_val = max(visited)
    idx = visited.index(max_val)

print(visited[idx])