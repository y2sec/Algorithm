# 배달

import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]

    for route in road:
        a, b, w = route
        graph[a].append([w, b])
        graph[b].append([w, a])

    def dijkstra(graph, start, N):
        townLeng = [float('inf') for _ in range(N + 1)]
        townLeng[start] = 0
        heap = []
        heapq.heappush(heap, [0, start])

        while heap:
            weight, currentTown = heapq.heappop(heap)

            if weight > townLeng[currentTown]:
                continue

            for adj, nextTown in graph[currentTown]:
                nextLeng = adj + weight
                if nextLeng <= townLeng[nextTown]:
                    townLeng[nextTown] = nextLeng
                    heapq.heappush(heap, [nextLeng, nextTown])

        return townLeng

    lengs = dijkstra(graph, 1, N)
    for leng in lengs:
        if leng <= K:
            answer += 1

    return answer
