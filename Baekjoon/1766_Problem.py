# 1766 문제집

import heapq

n, m = map(int, input().split())
result = []
parent = [0] * (n + 1)
array = [[] for x in range(n + 1)]

for _ in range(m):
    parent_node, child_node = map(int, input().split())
    array[parent_node].append(child_node)
    parent[child_node] += 1

heap = []

for idx in range(1, n + 1):
    if parent[idx] == 0:
        heapq.heappush(heap, idx)

while heap:
    problem = heapq.heappop(heap)
    result.append(problem)

    for child_node in array[problem]:
        parent[child_node] -= 1
        if parent[child_node] == 0:
            heapq.heappush(heap, child_node)

for problem in result:
    print(problem, end=" ")