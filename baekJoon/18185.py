import sys

n = int(sys.stdin.readline())
counts = list(map(int, sys.stdin.readline().rstrip("\n").split()))

#연속 구간을 받고 그게 한 층씩 빠지면서 얼마가 될 지 계산
# 2 4 3 0 2 -> [2 4 3][2]->2*7+1*5+1*3, 2*3 ->28
#[2 4 3] -> [4 3] -> [1]