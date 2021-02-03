# 11289 절대값 힙

from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if data != 0:
        heappush(heap, (abs(data), data))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)

