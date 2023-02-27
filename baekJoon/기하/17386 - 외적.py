import sys

input = sys.stdin.readline

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))


def CCW(l1, l2):
    vec1 = [l1[0] - l2[0], l1[1]-l2[1]]
    vec2 = [l1[2]-l2[0], l1[3] - l2[1]]
    vec3 = [l2[2] - l2[0], l2[3] - l2[1]]

    t1 = vec3[0] * vec1[1] - vec3[1] * vec1[0]
    t2 = vec3[0] * vec2[1] - vec3[1] * vec2[0]
    if t1 < 0 < t2 or t2 < 0 < t1:
        return True
    return False


if CCW(L1, L2) and CCW(L2, L1):
    print(1)
else:
    print(0)