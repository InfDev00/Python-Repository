import random
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j]:
            parent[find_parent(i)] = find_parent(j)

plan = list(map(int, sys.stdin.readline().split()))

ans = "YES"
srt = plan[0] - 1
for i in plan[1:]:
    if find_parent(i - 1) != find_parent(srt):
        ans = "NO"
        break
    srt = i-1
print(ans)
