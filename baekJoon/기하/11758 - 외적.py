import sys

p1 = list(map(int, sys.stdin.readline().split()))
p2 = list(map(int, sys.stdin.readline().split()))
p3 = list(map(int, sys.stdin.readline().split()))

vec1 = [p2[0] - p1[0], p2[1] - p1[1]]
vec2 = [p3[0] - p2[0], p3[1] - p2[1]]

ans = 0
t = vec1[0]*vec2[1]-vec1[1]*vec2[0]

if t < 0:
    ans = -1
elif t > 0:
    ans = 1

print(ans)