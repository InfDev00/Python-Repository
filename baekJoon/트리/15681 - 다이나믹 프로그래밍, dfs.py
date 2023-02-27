import sys
sys.setrecursionlimit(10**6)

n, r, q = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def DFS(cur):
    visited[cur] += 1
    for nxt in graph[cur]:
        if visited[nxt] == 0:
            visited[cur] += DFS(nxt)
    return visited[cur]


DFS(r)


for _ in range(q):
    tmp = int(sys.stdin.readline())
    print(visited[tmp])