import sys

INF = 2 ** 64 - 1
n, m = map(int, sys.stdin.readline().split())
buses = list()
dist = [INF] * (n + 1)

for _ in range(m):
    buses.append(list(map(int, sys.stdin.readline().split())))


def bellman(srt):
    dist[srt] = 0

    for i in range(n):
        for j in range(m):
            begin, arrive, time = buses[j]
            if dist[begin] != INF and dist[begin] + time < dist[arrive]:
                dist[arrive] = dist[begin] + time
                if i == n - 1:
                    return True
    return False


if bellman(1):
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] != INF else -1)
