import sys

hobit = list()
for _ in range(9):
    hobit.append(int(sys.stdin.readline()))

hobit.sort()

limit = sum(hobit)-100


find = False
for i in range(9):
    if find:
        break
    for j in range(i+1, 9):
        if find:
            break
        if hobit[i]+hobit[j] == limit:
            hobit[i], hobit[j] = 0, 0
            find = True

for i in range(9):
    if hobit[i] != 0:
        print(hobit[i])