import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
node = [0]+list(map(int, sys.stdin.readline().split()))
edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)

visited = [False for _ in range(n + 1)]
dp_non = [0 for _ in range(n + 1)]
dp_use = [0 for _ in range(n + 1)]


def DFS(cur):
    visited[cur] = True
    dp_use[cur] += node[cur]

    for nxt in edge[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            DFS(nxt)
            dp_non[cur] += max(dp_use[nxt], dp_non[nxt])
            dp_use[cur] += dp_non[nxt]


DFS(1)
ans = dp_non[1] if dp_non[1] > dp_use[1] else dp_use[1]
print(ans)