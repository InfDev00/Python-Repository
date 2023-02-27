import sys

n, m = map(int, sys.stdin.readline().split())
costs = list()
dots_code = dict()
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for idx in dots_code:
        c, d = dots_code[idx]
        dist = (a - c) ** 2 + (b - d) ** 2
        costs.append((dist ** (1 / 2), i, idx))
    dots_code.update({i: (a, b)})

costs.sort(key=lambda x: x[0], reverse=True)
parent = [i for i in range(n)]


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a-1, b-1)

ans = 0
while costs:
    c, a, b = costs.pop()
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c

print("%.2f" % ans)
