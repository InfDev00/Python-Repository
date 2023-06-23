import sys

n = int(sys.stdin.readline())
matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

DP = [[[0,0,0] for _ in range(n)] for _ in range(n)]


        


def CheckDiag(r,c):
    if CheckDown(r,c) and CheckRight(r,c):
        r+=1
        c+=1
        if matrix[r][c]==0:
            return True
    return False

def CheckDown(r,c):
    r+=1
    if CheckIn(r,c):
        if matrix[r][c]==0:
            return True
    return False

def CheckRight(r,c):
    c+=1
    if CheckIn(r,c):
        if matrix[r][c]==0:
            return True
    return False

def CheckIn(r,c):
    if 0<=r<n and 0<=c<n:
        return True
    return False

DP[0][1] = (1,0,0)
for Sum in range(1,2*n-1):
    for i in range(0,n):
        j = Sum-i

        if CheckRight(i,j):
            DP[i][j+1][0]+=DP[i][j][0]+DP[i][j][2]
        if CheckDown(i,j):
            DP[i+1][j][1]+=DP[i][j][1]+DP[i][j][2]
        if CheckDiag(i,j):
            DP[i+1][j+1][2]+=DP[i][j][0]+DP[i][j][1]+DP[i][j][2]


print(sum(DP[i][j]))