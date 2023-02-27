import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

ans = 0
arr.sort()


i, j = 0, n-1
while i < j:
    add = arr[i] + arr[j]
    if add == x:
        ans += 1
        i += 1
        j -= 1
    elif add > x:
        j -= 1
    else:
        i += 1

print(ans)
