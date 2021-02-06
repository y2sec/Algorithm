# 1504 특정한 최단 경로

import sys
import heapq


def dijkstra(start):
    distances = [[float('inf'), start] for _ in range(N+1)]
    distances[start] = [0, start]
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        curr_distance, curr_vertex = heapq.heappop(queue)

        if curr_distance > distances[curr_vertex][0]:
            continue

        for nxt_vertex, weight in graph[curr_vertex]:
            distance = curr_distance + weight
            if distances[nxt_vertex][0] > distance:
                distances[nxt_vertex][0] = distance
                heapq.heappush(queue, [distance, nxt_vertex])

    return distances


N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]


for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

v_distances = dijkstra(1)
v1_distances = dijkstra(v1)
v2_distances = dijkstra(v2)

route1 = v_distances[v1][0] + v1_distances[v2][0] + v2_distances[N][0]
route2 = v_distances[v2][0] + v2_distances[v1][0] + v1_distances[N][0]

print(min(route1, route2) if min(route1, route2) != float('inf') else -1)
