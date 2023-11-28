def fact(x:int, y:int):
    if x == 0:
        return y
    else:
        return fact(x-1, x*y)

def comb(n:int, m:int):
    return int(fact(n,1)/(fact(n-m,1)*fact(m, 1)))

t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    ans.append(comb(m,n))

for i in range(t):
    print(ans[i])