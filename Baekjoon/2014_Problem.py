# 2014 소수의 곱

import heapq
import copy

K, N = map(int, input().split())
lst = list(map(int, input().split()))

ck = set()
heap = copy.deepcopy(lst)
heapq.heapify(heap)

cnt = 0

while cnt < N:
    n = heapq.heappop(heap)
    if n in ck:
        continue
    ck.add(n)
    cnt += 1
    for i in lst:
        if n*i < 2**31 and n*i not in ck:
            heapq.heappush(heap, n*i)

print(n)
