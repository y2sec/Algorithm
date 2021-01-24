# 1715 카드 정렬하기

import heapq

heap = []
n = int(input())
result = 0
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while heap:
    A = heapq.heappop(heap)
    if heap:
        B = heapq.heappop(heap)
        result += A + B
        heapq.heappush(heap, A + B)

print(result)
