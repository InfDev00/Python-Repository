import sys
import math
input = sys.stdin.readline

n, red, green, blue = map(int, input().split())
# 코드 풀이 요약
# level이 3의 배수인 경우, 2의 배수인 경우, 1의 배수(default)인 경우에 따라 경우의 수 구함
# 매 level마다 반복해야 하며 전체 개수를 조절하면 안되므로 backtracking으로 구현
# 배치 순서도 고려해야 하므로 중복순열 및 조합 사용
def multinomial_permutation(n, counts): # 중복 순열 구현
    result = math.factorial(n)
    for count in counts:
        result //= math.factorial(count)
    return result

def backtrack(dep, r, g, b):
    if dep == 0:
        return 1
    
    ans = 0
    if dep % 3 == 0: # 3의 배수인 경우 -> red, green, blue에서 동일한 개수(depth/3)만큼 배치하는 경우의 수
        if r >= dep//3 and g >= dep//3 and b >= dep//3:
            ans+= backtrack(dep-1, r-dep//3, g-dep//3, b-dep//3) * multinomial_permutation(dep, [dep//3, dep//3, dep//3])
    
    if dep % 2 == 0: # 2의 배수인 경우 -> red, green, blue에서 2가지 색을 골라 동일한 개수(depth/2)만큼 배치하는 경우의 수
        if r >= dep//2 and g >= dep//2:
           ans+= backtrack(dep-1, r-dep//2, g-dep//2, b)* math.comb(dep, dep//2)
        if r >= dep//2 and b >= dep//2:
            ans += backtrack(dep-1, r-dep//2, g, b-dep//2)*math.comb(dep, dep//2)
        if g >= dep//2 and b >= dep//2:
            ans += backtrack(dep-1, r, g-dep//2, b-dep//2)*math.comb(dep, dep//2)
    
    if dep % 1 == 0: # default -> 단색으로 통일하는 경우의 수
        if r >= dep:
            ans += backtrack(dep-1, r-dep, g, b)
        if g >= dep:
            ans += backtrack(dep-1, r, g-dep, b)
        if b >= dep:
            ans += backtrack(dep-1, r, g, b-dep)

    return ans

print(backtrack(n, red, green, blue))