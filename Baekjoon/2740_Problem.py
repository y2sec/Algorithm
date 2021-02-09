# 2740 행렬 곱셈

import sys


N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for i in range(N):
    for j in range(K):
        print(C[i][j], end=' ')
    print()
