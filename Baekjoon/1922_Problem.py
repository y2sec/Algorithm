# 1922 네트워크 연결

import sys
import heapq


def find(computer):
    if parent[computer] == computer:
        return computer

    parent[computer] = find(parent[computer])
    return parent[computer]


def union(computerA, computerB):
    computerA = find(computerA)
    computerB = find(computerB)

    if computerA == computerB:
        return False

    parent[computerA] = computerB
    return True


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

heap = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, [c, a, b])

parent = [x for x in range(N + 1)]

result = 0
while heap:
    c, a, b = heapq.heappop(heap)

    if union(a, b):
        result += c


print(result)
