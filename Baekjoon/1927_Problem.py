# 1927 최소 힙

import heapq
import sys
heap = list()

n = int(input())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
