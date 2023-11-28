import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

n = n-1

if(n%(m+1)==0):
    print("Can't win")
else:
    print("Can win")