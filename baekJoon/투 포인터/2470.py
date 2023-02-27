import sys

n = int(sys.stdin.readline())
chemical = list(map(int, sys.stdin.readline().split()))

chemical.sort()


srt, end = 0, n - 1
min_val = int(2e9)
ret_idx = [-1, -1]

while srt < end:
    add = chemical[srt] + chemical[end]

    if abs(add) < abs(min_val):
        min_val = add
        ret_idx = [srt, end]

    if add < 0:
        srt += 1
    elif add > 0:
        end -= 1
    else:
        break

print(chemical[ret_idx[0]], chemical[ret_idx[1]])