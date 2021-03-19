# 근묵자흑

import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

N -= 1
answer = N // (K-1)
N %= (K-1)

print(answer if N == 0 else answer+1)
