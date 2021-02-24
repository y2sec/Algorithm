# 1197 최소 스패닝 트리

import sys
import heapq


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    A = find(a)
    B = find(b)

    if A == B:
        return False
    parent[A] = B
    return True


def mst(q):
    weight = 0
    while q:
        c, a, b = heapq.heappop(q)
        if union(a, b):
            weight += c

    return weight


V, E = map(int, sys.stdin.readline().split())
parent = [x for x in range(V+1)]
queue = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(queue, [C, A, B])

print(mst(queue))
