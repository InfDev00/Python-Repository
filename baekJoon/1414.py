import sys
input = sys.stdin.readline

def CtoI(c):
    if 'a'<=c<='z':
        return ord(c)-ord('a')+1 
    elif 'A'<=c<='Z':
        return ord(c)-ord('A')+27
    return 0

n = int(input())
mat = [[1e9]*n for _ in range(n)]
for i in range(n):
    s= input()
    for j in range(n):
        mat[i][j] = CtoI(s[j])

tree = []
for i in range(n):
    for j in range(n):
        tree.append((mat[i][j], i, j))
