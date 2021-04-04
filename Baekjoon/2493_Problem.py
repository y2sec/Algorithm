# 2493 탑

import heapq

N = int(input())
tops = list(map(int, input().split()))
topsConnect = [0 for _ in range(N)]
heap = []
heapq.heappush(heap, [tops[N-1], N-1])
for idx in range(N-2, -1, -1):
    while heap and tops[idx] >= heap[0][0]:
        height, topIdx = heapq.heappop(heap)
        topsConnect[topIdx] = idx+1

    heapq.heappush(heap, [tops[idx], idx])

for top in topsConnect:
    print(top, end=' ')
