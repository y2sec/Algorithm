# 9370 미확인 도착지

import sys
import heapq


def dijkstra(start):
    distances = [float('inf') for _ in range(n+1)]
    queue = []

    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        curr_distances, curr_vertex = heapq.heappop(queue)

        if curr_distances > distances[curr_vertex]:
            continue
        for nxt_vertex, weight in graph[curr_vertex]:
            distance = curr_distances + weight

            if distance < distances[nxt_vertex]:
                distances[nxt_vertex] = distance
                heapq.heappush(queue, (distance, nxt_vertex))

    return distances


T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    ans = []

    ghLen = 0

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if g in (a, b) and h in (a, b):
            ghLen = d

    res = dijkstra(s)
    resG = dijkstra(g)
    resH = dijkstra(h)

    for _ in range(t):
        x = int(sys.stdin.readline())

        if res[x] != float('inf') and res[x] == min(res[g] + ghLen + resH[x], res[h] + ghLen + resG[x]):
            ans.append(x)

    ans.sort()

    for x in ans:
        print(x, end=' ')
    print()
