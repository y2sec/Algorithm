# 1916 최소비용 구하기

import sys
import heapq


def dijkstra(busT, s):
    heap = []
    heapq.heappush(heap, [0, s])
    dist = [float('inf') for _ in range(N + 1)]
    dist[s] = 0

    while heap:
        l, curr = heapq.heappop(heap)
        if l > dist[curr]:
            continue

        for nxt, d in busT[curr]:
            nxtL = l + d
            if nxtL >= dist[nxt]:
                continue

            dist[nxt] = nxtL
            heapq.heappush(heap, [nxtL, nxt])

    return dist


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

busTerminate = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    busTerminate[a].append([b, c])

S, E = map(int, sys.stdin.readline().split())
dist = dijkstra(busTerminate, S)
print(dist[E])
