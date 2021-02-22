# 20951 유아와 곰두리차

import sys

N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)

dp = [[0 for _ in range(8)] for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = 1

for i in range(1, 8):
    for j in range(1, N+1):
        for k in edge[j]:
            dp[j][i] += dp[k][i-1]

ans = 0
for d in dp:
    ans += d[7]

print(ans % 1000000007)
