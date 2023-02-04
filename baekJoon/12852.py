import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [0 for _ in range(n + 1)]
queue = deque([1])

while queue:
    cur = queue.popleft()
    if cur == n:
        break

    for i in range(1, 4):
        nxt = cur * i if i != 1 else cur + 1
        if nxt <= n and arr[nxt] == 0:
            queue.append(nxt)
            arr[nxt] = cur


idx = n
ans = []
while idx:
    ans.append(idx)
    idx = arr[idx]

print(len(ans)-1)
print(*ans)