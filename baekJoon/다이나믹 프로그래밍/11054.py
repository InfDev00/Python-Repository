n = int(input())
array = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]

for i in range(n):
    value = array[i]
    for j in range(i):
        if array[j] < value and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

for i in range(n-1, -1, -1):
    value = array[i]
    for j in range(n-1, i, -1):
        if array[j] < value and dp2[j]+1 > dp2[i]:
            dp2[i] = dp2[j]+1            

for i in range(n):
    dp[i]+=dp2[i]
    
print(max(dp)-1)