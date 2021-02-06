# 1753 최단경로

import sys
import heapq


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
length = [[float('inf'), K] for _ in range(V+1)]
queue = []


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

length[K] = [0, K]
heapq.heappush(queue, [0, K])

while queue:
    cur_len, cur_ver = heapq.heappop(queue)

    if length[cur_ver][0] < cur_len:
        continue

    for v, w in graph[cur_ver]:
        leng = cur_len + w
        if length[v][0] > leng:
            length[v] = [leng, cur_ver]
            heapq.heappush(queue, [leng, v])

for i in range(1, V+1):
    if length[i][0] == float('inf'):
        print('INF')
    else:
        print(length[i][0])
