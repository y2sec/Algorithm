# 11657 타임머신

import sys

N, M = map(int, sys.stdin.readline().split())
bus = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
city = [float('inf') for _ in range(N+1)]
city[1] = 0
for i in range(N):
    change = False
    for a, b, c in bus:
        leng = city[a] + c
        if leng < city[b]:
            change = True
            city[b] = leng
    if i == N-1 and change:
        print(-1)
        exit()

for i in range(2, N+1):
    if city[i] == float('inf'):
        print(-1)
    else:
        print(city[i])
