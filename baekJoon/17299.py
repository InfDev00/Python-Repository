import sys
from collections import deque

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
F = dict()
stack = list()
ans = [0]*n

for _ in range(n):
    tmp = lst.pop()
    F[tmp] = 1 if tmp not in F else F[tmp] + 1
    stack.append(tmp)

for _ in range(n):
    tmp = stack.pop()
    lst.append(tmp)

for i in range(n-1, -1, -1):
    num = lst[i]
    height = F[num]
    while len(stack) != 0 and height >= F[lst[stack[len(stack)-1]]]:
        stack.pop()
    ans[i] = -1 if len(stack) == 0 else lst[stack[len(stack)-1]]
    stack.append(i)

for i in range(n):
    print(ans[i], end=" ")