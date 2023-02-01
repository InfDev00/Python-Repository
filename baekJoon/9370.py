import sys
from collections import deque

T = int(sys.stdin.readline())
INF = int(1e9)

costs = []
roads = []
visited = []
arrives = []


def dijkstra(srt, l):
    global costs, visited
    costs = [INF for _ in range(l + 1)]
    visited = [False for _ in range(l + 1)]
    costs[srt] = 0
    queue = deque()
    queue.append(srt)

    while len(queue) != 0:
        cur = queue.popleft()
        visited[cur] = True
        for tmp in roads[cur]:
            nxt, nxt_cost = tmp[0], tmp[1]
            if not visited[nxt]:
                costs[nxt] = min(costs[nxt], costs[cur] + nxt_cost)

        min_cost = INF
        nxt_srt = -1
        for i in range(1, l+1):
            if min_cost > costs[i] and visited[i] != True:
                min_cost = costs[i]
                nxt_srt = i

        if nxt_srt != -1:
            queue.append(nxt_srt)


for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    roads = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    costs = [INF for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        roads[a].append([b, d])
        roads[b].append([a, d])
    arrives = list()
    for _ in range(t):
        arrives.append(int(sys.stdin.readline()))

    dijkstra(s, n)
    shortest_path = costs.copy()

    first_spot = g if costs[g] < costs[h] else h
    s_to_f = costs[first_spot]

    dijkstra(first_spot, n)

    second_spot = g if first_spot != g else h
    f_to_s = costs[second_spot]

    dijkstra(second_spot, n)

    prt_lst = list()
    for i in range(t):
        cur = arrives[i]
        if shortest_path[cur] == s_to_f + f_to_s + costs[cur]:
            prt_lst.append(cur)

    prt_lst.sort()

    for i in prt_lst:
        print(i, end=" ")
