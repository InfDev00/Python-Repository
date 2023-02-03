import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr_sum = [0]
for i in range(n):
    arr_sum.append(arr_sum[i] + arr[i])


srt, end = 0, 1
ans = int(1e9)

while srt < end < n+1:
    add = arr_sum[end] - arr_sum[srt]

    if add < s:
        end += 1
    else:
        if end - srt < ans:
            ans = end - srt
        srt += 1

if ans == int(1e9):
    ans = 0
print(ans)
