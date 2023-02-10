import sys

INF = int(2e9)
v, e = map(int, sys.stdin.readline().split())
costs = list()
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    costs.append((c, a, b))

costs.sort(key=lambda x: x[0], reverse=True)

ans = 0
parent = [i for i in range(v + 1)]


def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


while costs:
    c, a, b = costs.pop()
    if find_parent(a) == find_parent(b):
        continue
    union(a, b)
    ans += c

print(ans)
