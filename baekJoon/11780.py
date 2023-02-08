import sys

INF = int(2e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
route = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
path = [[[i, j] for j in range(n + 1)] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    route[a][b] = min(route[a][b], c)

for i in range(1, n + 1):
    route[i][i] = 0

for stopover in range(1, n + 1):
    for srt in range(1, n + 1):
        for arrive in range(1, n + 1):
            if route[srt][stopover] + route[stopover][arrive] < route[srt][arrive]:
                route[srt][arrive] = route[srt][stopover] + route[stopover][arrive]
                path[srt][arrive] = path[srt][stopover]+path[stopover][arrive][1:]

for i in range(n + 1):
    for j in range(n + 1):
        if route[i][j] == INF:
            route[i][j] = 0

for i in range(1, n + 1):
    print(*route[i][1:])

for i in range(1, n + 1):
    for j in range(1, n+1):
        if route[i][j] == 0:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])