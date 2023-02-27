import sys

n = int(sys.stdin.readline())
Xs = list()
Ys = list()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    Xs.append(x)
    Ys.append(y)

Xs.append(Xs[0])
Ys.append(Ys[0])
ans = 0
for i in range(n):
    ans += Xs[i] * Ys[i+1] - Xs[i+1] * Ys[i]

print(abs(ans)/2)