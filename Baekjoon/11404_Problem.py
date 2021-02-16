# 11404 플로이드

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
dist = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a][b] = min(adj[a][b], c)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            dist[i][j] = 0
        elif adj[i][j] != float('inf'):
            dist[i][j] = adj[i][j]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
