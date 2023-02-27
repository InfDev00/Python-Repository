import sys

m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    tmp = sys.stdin.readline().strip("\n").split()
    x = tmp[0]
    y = 0
    if x == "add" or x == "remove" or x == "check" or x == "toggle":
        y = 1 << int(tmp[1]) - 1

    if x == "add":
        s = s | y
    elif x == "remove":
        s = s & ~y
    elif x == "check":
        print(1 if s & y != 0 else 0)
    elif x == "toggle":
        s = s ^ y
    elif x == "all":
        s = ~(1 << 20)
    elif x == "empty":
        s = 0
