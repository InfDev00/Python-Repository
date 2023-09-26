import sys

num = int(sys.stdin.readline())
numList = []

for _ in range(num):
	x, y = map(int, sys.stdin.readline().split())
	numList.append((x,y))

numList.sort(key = lambda x : (-x[0], -x[1]))

for _ in range(num):
	print(*numList.pop())