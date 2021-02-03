# 1655 가운데를 말해요

"""
중간 값을 구하는 방법
maxheap과 minheap 구현

maxheap의 크기는 minheap의 크기와 같거나 1 더 큼
minheap의 최소 값은 maxheap의 최대 값보다 크거나 같음

두 가지 조건이 충족할 때 중간 값은 maxheap의 최대 값
"""

import sys
import heapq

N = int(sys.stdin.readline())
maxheap = []
minheap = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, (-data, data))
    else:
        heapq.heappush(minheap, data)

    if len(minheap) > 0 and minheap[0] < maxheap[0][1]:
        minV = heapq.heappop(minheap)
        maxV = heapq.heappop(maxheap)[1]

        heapq.heappush(minheap, maxV)
        heapq.heappush(maxheap, (-minV, minV))

    print(maxheap[0][1])
