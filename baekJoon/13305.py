import sys

n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
prices.pop()
ans = 0


left_road = [0]
for i in range(n-1):
    tmp = roads.pop()
    left_road.append(tmp+left_road[i])

left_road.reverse()
left_road.pop()

drove_road = 0
while prices:
    min_price = min(prices)
    idx = prices.index(min_price)

    ans += min_price*(left_road[idx]-drove_road)
    prices = prices[:idx]
    drove_road = left_road[idx]

print(ans)
