# 2981 검문

import math


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


N = int(input())
lst = [int(input()) for _ in range(N)]
M = set()
lst.sort()

n = lst[1] - lst[0]
for i in range(2, N):
    n = gcd(n, lst[i] - lst[i - 1])

M.add(n)

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        M.add(i)
        M.add(n // i)

M = sorted(M)
for i in M:
    print(i, end=' ')
