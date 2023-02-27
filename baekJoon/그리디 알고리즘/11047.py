import sys

n, k = map(int, sys.stdin.readline().split())
money = list()
cnt = 0

for _ in range(n):
    money.append(int(sys.stdin.readline()))

for _ in range(n):
    t = money.pop()
    if t > k:
        continue
    else:
        cnt += k//t
        k = k % t

print(cnt)