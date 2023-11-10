import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 코드풀이 요약
# 보석과 가방을 무게 순으로 정렬
# 추출된 보석은 가치 순으로 정렬
# 이때 현재 가방 및 현재 가방보다 가벼운 가방에 담을 수 있는 보석만 추출하였으므로
# 가치만 고려하여도 됨
# 따라서 가방에 담을 수 있는 보석 중 가장 비싼 보석들만 추출하여서 그 값을 ans에 더함 

n, k = map(int, input().split())
priority_queue = []
bags = []
ans = 0
for _ in range(n):
    weight, value = map(int, input().split())
    heappush(priority_queue, (weight, value)) # 보석 값을 가벼운 것 우선으로 queue에 입력

for _ in range(k):
    bags.append(int(input()))

bags.sort() # 가장 적은 무게를 담는 가방부터 확인하기 위해 정렬

jewels = []
for bag in bags:
    while priority_queue and priority_queue[0][0] <= bag: # 현재 가방에 담을 수 있는 보석들 추출
        w, v = heappop(priority_queue)
        heappush(jewels, (-v, w)) # 추출된 보석을 가치 순으로 정렬

    if jewels:
        ans-=heappop(jewels)[0] # 추출된 보석 중 가장 비싼 보석 추출

print(ans)