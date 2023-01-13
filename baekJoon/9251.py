import sys

str1 = sys.stdin.readline().rstrip('\n')
str2 = sys.stdin.readline().rstrip('\n')

ans_list = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            ans_list[i+1][j+1] = ans_list[i][j]+1
        else:
            ans_list[i+1][j+1] = max(ans_list[i+1][j], ans_list[i][j+1])

print(ans_list[len(str1)][len(str2)])
