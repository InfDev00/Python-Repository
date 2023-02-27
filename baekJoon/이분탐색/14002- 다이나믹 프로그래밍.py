import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = list()
arr_idx = [-1 for _ in range(n)]


def binary_search(l, r, t):
    while l < r:
        mid = (l + r) // 2
        if ans[mid] < t:
            l = mid + 1
        else:
            r = mid
    return l


for i in range(n):
    cur = arr[i]
    idx = binary_search(0, len(ans), cur)
    arr_idx[i] = idx
    if idx < len(ans):
        ans[idx] = cur
    else:
        ans.append(cur)

idx = len(ans)-1
for i in range(n-1, -1, -1):
    if idx == arr_idx[i]:
        ans[idx] = arr[i]
        idx -= 1

print(len(ans))
print(*ans)