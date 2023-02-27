import sys

n = int(sys.stdin.readline())
arr = list(i for i in range(n+1))

arr[1] = 0
for i in range(2, n+1):
    for j in range(2*i, n+1, i):
        arr[j] = 0

Primes = list()

for i in range(n+1):
    if arr[i] != 0:
        Primes.append(arr[i])

Primes_sum = [0]
for i in range(len(Primes)):
    Primes_sum.append(Primes_sum[i] + Primes[i])

srt, end = 0, 1
ans = 0

while srt < end < len(Primes_sum):
    add = Primes_sum[end] - Primes_sum[srt]
    if add < n:
        end += 1
    elif add > n:
        srt += 1
    else:
        ans += 1
        srt += 1

print(ans)
