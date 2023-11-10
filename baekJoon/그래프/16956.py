import sys
input = sys.stdin.readline



sheep_list = []
R, C = map(int, input().split())
graph:list = []
for i in range(R):
    sk = list(input().strip("\n"))
    graph.append(sk)
    for j in range(C):
        if sk[j] == "S":
            sheep_list.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ans = 1

def printGraph():
    print(ans)
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end="")
        print()

for sheep in sheep_list:
    x, y = sheep
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >=0 and nx<R and ny >=0 and ny<C:
            if graph[nx][ny]=="W":
                ans = 0
                print(ans)
                sys.exit(0)
            if graph[nx][ny]!="S":
                graph[nx][ny]="D"

printGraph()