import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip("\n").split())))

def moveLeft():
    newBoard = []
    for line in board:
        newLine = []
        tmp = -1
        changed = False
        for i in line:
            if i == tmp and i != 0 and not changed:
                i*=2
                newLine[-1] = i
                tmp=i
                changed = True
            elif i != 0:
                newLine.append(i)
                tmp = i
                changed = False
        for i in range(len(line)-len(newLine)):
            newLine.append(0)
        newBoard.append(newLine)
    return newBoard

def moveRight():
    newBoard = []
    for line in board:
        line.reverse()
        newLine = []
        tmp = -1
        changed = False
        for i in line:
            if i == tmp and i != 0 and not changed:
                i*=2
                newLine[-1] = i
                tmp=i
                changed = True
            elif i != 0:
                newLine.append(i)
                tmp = i
                changed = False
        for i in range(len(line)-len(newLine)):
            newLine.append(0)
        newLine.reverse()
        newBoard.append(newLine)
    return newBoard

def moveDown():
    newBoard = []
    _board = list(map(list, zip(*board[::-1])))
    for line in _board:
        newLine = []
        tmp = -1
        changed = False
        for i in line:
            if i == tmp and i != 0 and not changed:
                i*=2
                newLine[-1] = i
                tmp=i
                changed = True
            elif i != 0:
                newLine.append(i)
                tmp = i
                changed = False
        for i in range(len(line)-len(newLine)):
            newLine.append(0)
        newBoard.append(newLine)
    return list(map(list, zip(*newBoard)))[::-1]

def moveUp():
    newBoard = []
    _board = list(map(list, zip(*board)))[::-1]
    for line in _board:
        newLine = []
        tmp = -1
        changed = False
        for i in line:
            if i == tmp and i != 0 and not changed:
                i*=2
                newLine[-1] = i
                tmp=i
                changed = True
            elif i != 0:
                newLine.append(i)
                tmp = i
                changed = False
        for i in range(len(line)-len(newLine)):
            newLine.append(0)
        newBoard.append(newLine)
    return list(map(list, zip(*newBoard[::-1])))

def print_box(box):
    if type(box) is dict:
        for i in box:
            print(i, box[i])
    elif type(box) is list:
        for i in box:
            print(i)

cnt = 0
_board = board.copy()
print_box(_board)
while True:
    cnt+=1
    print("-"*20)
    print("Enter the way U,D,R,L or END or RESET")
    inp = sys.stdin.readline().rstrip("\n")
    match inp:
        case "U":
            board = moveUp()
        case "D":
            board = moveDown()
        case "R":
            board = moveRight()
        case "L":
            board = moveLeft()
        case "END":
            break
        case "RESET":
            board = _board
            cnt = 0
    print_box(board)
    print(cnt)