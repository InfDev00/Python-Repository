import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n + 1)
dp_use = [0] * (n + 1)
dp_non = [0] * (n + 1)


def DFS(cur):
    visited[cur] = True
    dp_use[cur] += 1

    for nxt in tree[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            DFS(nxt)
            dp_use[cur] += min(dp_use[nxt], dp_non[nxt])
            dp_non[cur] += dp_use[nxt]

DFS(1)
print(min(dp_use[1], dp_non[1]))