# 18352 특정 거리의 도시 찾기

import sys
import heapq


def dijkstra(cities, start, maps):
    distances = [float('inf') for _ in range(cities + 1)]
    distances[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        distance, current = heapq.heappop(heap)

        if distances[current] < distance:
            continue

        for nxt in maps[current]:
            nxtDistance = distance + 1
            if distances[nxt] > nxtDistance:
                distances[nxt] = nxtDistance
                heapq.heappush(heap, [nxtDistance, nxt])

    return distances


N, M, K, X = map(int, sys.stdin.readline().split())

maps = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    maps[A].append(B)

result = dijkstra(N, X, maps)

if result.count(K) == 0:
    print(-1)

for city in range(1, N+1):
    if result[city] == K:
        print(city)
