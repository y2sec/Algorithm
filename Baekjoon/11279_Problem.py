# 11279 최대 힙

import heapq
import sys

queue = []
heapq.heapify(queue)

N = int(sys.stdin.readline())
for _ in range(N):
    data = int(sys.stdin.readline())
    if data != 0:
        heapq.heappush(queue, (-data, data))
    else:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
