import sys

n = int(sys.stdin.readline())

rock = [0 for _ in range(n)]

rock[0] = 1
for i in range(n):
    if(i+1 < n):
        rock[i+1] = rock[i]*(-1)
    if(i+3 < n):
        rock[i+3] = rock[i]*(-1)

if(rock[n-1] == 1):
    print("SK")
else:
    print("CY")