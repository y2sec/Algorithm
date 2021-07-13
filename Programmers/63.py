# 가장 먼 노드
import heapq


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    adj = [float('inf') for _ in range(n+1)]
    adj[1] = 0

    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        l, c = heapq.heappop(heap)

        if adj[c] < l:
            continue

        for nxt in graph[c]:
            nxtL = l + 1
            if nxtL >= adj[nxt]:
                continue

            adj[nxt] = nxtL
            heapq.heappush(heap, (nxtL, nxt))

    adj.sort(reverse=True)
    for idx in range(1, n+1):
        if adj[1] == adj[idx]:
            answer += 1
            continue
        break

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
