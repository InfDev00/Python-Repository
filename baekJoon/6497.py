import sys


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


while True:
    m, n = map(int, sys.stdin.readline().split())
    if (m, n) == (0, 0):
        break
    costs = list()
    parent = [i for i in range(m)]
    for _ in range(n):
        costs.append(tuple(map(int, sys.stdin.readline().split())))
    costs.sort(key=lambda x: x[2], reverse=True)

    ans = 0
    for i in range(n):
        ans+=costs[i][2]

    while costs:
        x, y, z = costs.pop()
        if find(x) == find(y):
            continue
        union(x, y)
        ans -= z
    print(ans)
