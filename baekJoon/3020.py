import sys

n, h = map(int, sys.stdin.readline().split())
top, bot = list(), list()
for i in range(n):
    if i % 2 == 0:
        bot.append(int(sys.stdin.readline()))
    else:
        top.append(h - int(sys.stdin.readline()))


def merge_sort(l, r, ret):
    if l < r:
        mid = (l + r) // 2
        merge_sort(l, mid, ret)
        merge_sort(mid + 1, r, ret)
        merge(l, r, mid, ret)


def merge(l, r, mid, ret):
    x, y = l, mid + 1
    ans = list()
    while x <= mid and y <= r:
        if ret[x] < ret[y]:
            ans.append(ret[x])
            x += 1
        else:
            ans.append(ret[y])
            y += 1
    while x <= mid:
        ans.append(ret[x])
        x += 1
    while y <= r:
        ans.append(ret[y])
        y += 1
    for j in range(l, r + 1):
        ret[j] = ans[j - l]


merge_sort(0, n // 2 - 1, bot)
merge_sort(0, n // 2 - 1, top)


def binary(l, r, cur, lst, ans):
    if l > r:
        return ans
    else:
        mid = (l + r) // 2
        if lst[mid] < cur:
            return binary(mid + 1, r, cur, lst, mid + 1)
        elif lst[mid] > cur:
            return binary(l, mid - 1, cur, lst, ans)
        else:
            if mid == 0:
                return mid
            elif lst[mid - 1] < cur:
                return mid
            else:
                return binary(l, mid - 1, cur, lst, mid)


min = n
min_cnt = 0
for i in range(1, h + 1):
    ret = binary(0, n // 2 - 1, i, top, 0) + n // 2 - binary(0, n // 2 - 1, i, bot, 0)
    if ret < min:
        min = ret
        min_cnt = 1
    elif ret == min:
        min_cnt += 1

print(min, min_cnt)
