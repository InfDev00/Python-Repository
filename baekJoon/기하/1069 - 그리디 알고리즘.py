import sys
from math import sqrt

x, y, d, t = map(int, sys.stdin.readline().split())

dist = sqrt(x ** 2 + y ** 2)
ans = 0
if dist > d:
    cnt = dist//d
    ans = min(dist, cnt*t+dist-cnt*d, (cnt+1)*t)
else:
    ans = min(2*t, t+d-dist, dist)

print(ans)