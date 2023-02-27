import sys

s = sys.stdin.readline().rstrip("\n")
n = int(sys.stdin.readline())

alp_box = dict()
ans_list = list()
for i in range(len(s)):
    if s[i] not in alp_box:
        alp_box[s[i]] = [0 for _ in range(len(s))]
    alp_box[s[i]][i] = 1

for alp in alp_box:
    now = 0
    for i in range(len(alp_box[alp])):
        now += alp_box[alp][i]
        alp_box[alp][i] = now


for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    l, r = int(l), int(r)

    if a not in alp_box:
        ans_list.append(0)
        continue

    ans = alp_box[a]
    left = ans[l-1] if l > 0 else 0
    right = ans[r]
    ans_list.append(right - left)

for j in range(n):
    print(ans_list[j])
