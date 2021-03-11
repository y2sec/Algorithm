# 10159 저울

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

stuff = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    stuff[a][b] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if stuff[i][j] or (stuff[i][k] and stuff[k][j]):
                stuff[i][j] = True

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if not stuff[i][j] and not stuff[j][i]:
            cnt += 1
    print(cnt)
