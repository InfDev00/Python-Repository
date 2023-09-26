import sys

num1, num2 = map(list, sys.stdin.readline().split())
num1.reverse()
num2.reverse()

num1 = ''.join(num1)
num2 = ''.join(num2)

num1 = int(num1)
num2 = int(num2)

print(max(num1, num2))