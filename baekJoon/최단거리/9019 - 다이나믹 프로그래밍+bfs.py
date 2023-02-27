import sys
from collections import deque

t = int(sys.stdin.readline())
steps = ['D', 'S', 'L', 'R']
ans_lst = list()
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    visited = [int(2e9) for _ in range(10000)]
    cal = ["" for _ in range(10000)]
    queue = deque([a])
    visited[a] = 0
    while queue:
        cur = queue.popleft()
        if cur == b:
            break

        nxt = [(2 * cur) % 10000, cur - 1 if cur > 0 else 9999, (cur * 10) % 10000 + (cur * 10) // 10000,
               (cur % 10) * 1000 + cur // 10]
        for i in range(4):
            if visited[nxt[i]] == int(2e9):
                cal[nxt[i]] = steps[i]
                visited[nxt[i]] = cur
                queue.append(nxt[i])

    ans = ""
    idx = b
    while idx != a:
        ans = cal[idx]+ans
        idx = visited[idx]
    ans_lst.append(ans)

for i in range(t):
    print(ans_lst[i])
