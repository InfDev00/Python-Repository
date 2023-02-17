import sys
from math import sqrt

arr = list(map(int, sys.stdin.readline().split()))

SIZE = 8
visited = [False] * SIZE
x = 0
ans = 0


def check(a, b, c):
    y, x = max(a, c), min(a, c)
    if sqrt(2) * x * y / (x + y) > b:
        return False
    return True


def perm(cur, lst):
    global ans
    global x
    visited[cur] = True
    lst.append(arr[cur])
    if len(lst) == SIZE:
        lst.extend(lst[0:2].copy())
        x += 1
        chk = True
        for i in range(SIZE):
            if not check(lst[i], lst[i + 1], lst[i + 2]):
                chk = False
        if chk:
            ans += 1
        lst.pop()
        lst.pop()
        return

    for i in range(SIZE):
        if not visited[i]:
            perm(i, lst)
            visited[i] = False
            lst.pop()


for i in range(SIZE):
    perm(i, [])
    visited[i] = False

print(ans)
