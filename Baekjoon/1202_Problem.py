# 1202 보석 도둑

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewelries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

jewelries.sort(key=lambda x:x[0])
bags.sort()

value = 0
heap = []
idx = 0
for bag in bags:
    while idx < N and bag >= jewelries[idx][0]:
        heapq.heappush(heap, -jewelries[idx][1])
        idx += 1
    if heap:
        value += heapq.heappop(heap)

print(-value)
