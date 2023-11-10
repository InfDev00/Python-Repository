import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

def BFS(i):
    visited = [False for _ in range(n+1)]
    queue = deque([i])
    step = 0
    visited[i] = True
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            for friend in graph[current]:
                if not visited[friend]:
                    queue.append(friend)
                    visited[friend] = True
        step+=1
    return step




while True:
    x, y = map(int, input().split())
    if x==-1 and y==-1:
        break
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    score = BFS(i)
    print(score)