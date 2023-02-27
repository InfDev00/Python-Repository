import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lst = [int(1e9) for _ in range(n)]
ans = 0


def binary_search(x):
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if lst[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


for cur in arr:
    idx = binary_search(cur)
    ans = idx if idx > ans else ans
    lst[idx] = cur

print(ans + 1)
