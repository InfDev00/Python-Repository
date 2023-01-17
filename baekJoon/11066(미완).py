import sys

t = int(sys.stdin.readline().strip('\n'))

def get_min(x, y, box):
    m = 2**31-1
    for i in range(x, y):
        a = box[x][i] + box[1 + i][y]
        if a < m:
            m = a
    return m


def func(n, lst):
    sums = list()
    sums.append(0)
    for i in range(n):
        sums.append(sums[i]+lst[i])

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n): #gap
        for i in range(n - j):
            matrix[i][i + j] = get_min(i, i + j, matrix) + sums[i+j+1]-sums[i]

    print(matrix[0][n-1])


for _ in range(t):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    func(k, files)
