import sys
input = sys.stdin.readline

def multiply(A:str, B:str):
    ans = "0"
    for i in range(len(A)):
        for j in range(len(B)):
            ans = summation(ans, str(int(A[i]) * int(B[j])*(10**i)*(10**j)))
    return ans

            
def summation(A:str, B:str):
    ans = ""
    tmp = 0
    if(len(A) <= len(B)):
        A = "0"*(len(B)-len(A)) + A
    else:
        B = "0"*(len(A)-len(B)) + B
    while len(A) > 0:
        int_A = int(A[-1])
        int_B = int(B[-1])
        tmp += int_A + int_B
        ans = str(tmp % 10)+ans
        tmp //= 10
        A = A[:-1]
        B = B[:-1]

    if tmp > 0:
        ans = str(tmp)+ans
    return ans

if __name__ == '__main__':
    A, B = input().split()

    print(multiply(A, B))