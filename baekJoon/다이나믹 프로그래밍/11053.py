n = int(input())
array = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    value = array[i]
    for j in range(i):
        if array[j] < value and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
            

print(max(dp))