import sys
from collections import deque

lines = list()
bip = list()
ans = "YES"


def BFS(srt):
    global ans
    queue = deque()
    side = deque()
    queue.append(srt)
    side.append(1)

    while len(queue) != 0:
        cur = queue.popleft()
        cur_side = side.popleft()

        while len(lines[cur]) != 0:
            nxt = lines[cur].pop()
            if nxt == cur:
                ans = "NO"
                return

            if bip[nxt] == 0:
                bip[nxt] = -cur_side
            elif bip[nxt] != -cur_side:
                ans = "NO"
                return
            queue.append(nxt)
            side.append(-cur_side)


k = int(sys.stdin.readline())
for _ in range(k):
    ans = "YES"
    v, e = map(int, sys.stdin.readline().split())
    lines = [[] for _ in range(v + 1)]
    bip = [0 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        lines[a].append(b)
        lines[b].append(a)

    for i in range(1, v+1):
        BFS(i)
    print(ans)
