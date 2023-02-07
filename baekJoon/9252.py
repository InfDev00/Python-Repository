import sys

str1 = sys.stdin.readline().rstrip('\n')
str2 = sys.stdin.readline().rstrip('\n')
ans_list = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            ans_list[i + 1][j + 1] = ans_list[i][j] + 1

        else:
            ans_list[i + 1][j + 1] = max(ans_list[i + 1][j], ans_list[i][j + 1])

ans = ""
x, y = len(str1) - 1, len(str2) - 1
while x >= 0 and y >= 0:
    if str1[x] == str2[y]:
        ans = str1[x] + ans
        x, y = x - 1, y - 1
    else:
        if ans_list[x][y + 1] > ans_list[x + 1][y]:
            x -= 1
        else:
            y -= 1

print(ans_list[len(str1)][len(str2)])
print(ans)
