# 1956 운동

import sys

V, E = map(int, sys.stdin.readline().split())
adj = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]
dist = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = adj[i][j]

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

res = float('inf')

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            continue
        res = min(res, dist[i][j] + dist[j][i])

print(res if res != float('inf') else -1)
