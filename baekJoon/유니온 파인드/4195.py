import sys


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

ans = []
t = int(sys.stdin.readline())
for _ in range(t):
    friend_code = dict()
    idx = 0
    parent = list()
    group = list()
    f = int(sys.stdin.readline())
    for _ in range(f):
        a, b = sys.stdin.readline().rstrip("\n").split()
        if a not in friend_code:
            friend_code[a] = idx
            parent.append(idx)
            group.append(1)
            idx += 1
        if b not in friend_code:
            friend_code[b] = idx
            parent.append(idx)
            group.append(1)
            idx += 1

        a = friend_code[a]
        b = friend_code[b]
        f_a, f_b = find_parent(a), find_parent(b)
        parent[f_a] = f_b
        if f_a != f_b:
            group[f_b] += group[f_a]

        ans.append(group[f_b])

for i in ans:
    print(i)

