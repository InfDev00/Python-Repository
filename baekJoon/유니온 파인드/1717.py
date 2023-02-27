import sys
sys.setrecursionlimit(10**5)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c:
        print("YES") if find_parent(a) == find_parent(b) else print("NO")
    else:
        parent[find_parent(a)] = find_parent(b)
