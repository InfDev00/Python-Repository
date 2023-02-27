import sys

sys.setrecursionlimit(100000)


def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

ans = 0
for t in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    parent_a, parent_b = find_parent(a), find_parent(b)
    if parent_a == parent_b:
        ans = t
        break
    elif parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a


print(ans)