import sys
input = sys.stdin.readline

def CtoI(c):
    if 'a'<=c<='z':
        return ord(c)-ord('a')+1 
    elif 'A'<=c<='Z':
        return ord(c)-ord('A')+27
    return 0

def find_parent(parent, x):
    if parent[x]!=x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
mat = [[1e9]*n for _ in range(n)]
for i in range(n):
    s= input()
    for j in range(n):
        mat[i][j] = CtoI(s[j])


edge = []
for i in range(n):
    for j in range(n):
        edge.append((mat[i][j], i, j))
edge.sort(key=lambda x: x[0])

node = [x for x in range(n)]

len_sum = 0
for e in edge:
    len_sum+= e[0]

for e in edge:
    if find_parent(node, e[1])!=find_parent(node, e[2]) and e[0] != 0:
        len_sum-=e[0]
        union_parent(node, e[1], e[2])

flag = True
for n in node:
    if n!= node[0]:
        flag = False
        break
if flag:
    print(len_sum)
else:
    print(-1)