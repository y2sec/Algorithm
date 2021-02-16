# 10217 KCM Travel

import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    tickets = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        tickets[u].append([v, c, d])
    queue = []
    adj = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    adj[1][0] = 0
    for i in range(M+1):
        for j in range(1, N+1):
            if adj[j][i] == float('inf'):
                continue

            for v, c, d in tickets[j]:
                if i + c > M:
                    continue
                adj[v][i+c] = min(adj[v][i+c], adj[j][i] + d)

    res = min(adj[N])
    print(res if res != float('inf') else 'Poor KCM')
