import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue(maxsize=n)
for _ in range(n):
    queue.put(int(input()))

ans = 0
while queue.qsize() > 1:
    x1 = queue.get()
    x2 = queue.get()
    queue.put(x1+x2)
    ans+=x1+x2
print(ans)