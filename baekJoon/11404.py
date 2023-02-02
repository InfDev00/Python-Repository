import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
path = [[] for _ in range(n+1)]
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if dist[a][b] > c:
        path[a].append([b, c])
        dist[a][b] = c

for i in range(1, n+1):
    dist[i][i] = 0


for stopover in range(1, n+1):
    for nxt in range(1, n+1):
        for cur in range(1, n+1):
            dist[cur][nxt] = min(dist[cur][nxt], dist[cur][stopover]+dist[stopover][nxt])

for i in range(1, n+1):
    for j in range(1, n+1):
        dist[i][j] = 0 if dist[i][j] == INF else dist[i][j]
        print(dist[i][j], end=" ")
    print()
######11404