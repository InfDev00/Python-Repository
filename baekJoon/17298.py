import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = list()

ans = [0]*n
for i in range(n-1, -1, -1):
    tmp = lst.pop()
    while len(stack) != 0 and stack[len(stack)-1] <= tmp:
        stack.pop()

    ans[i] = stack[len(stack)-1] if len(stack)!= 0 else -1
    stack.append(tmp)

for i in range(n):
    print(ans[i], end=" ")