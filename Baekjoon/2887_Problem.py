# 2887 행성 터널

import sys
import heapq


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    A = find(a)
    B = find(b)

    if A == B:
        return False
    parent[A] = B
    return True


def two_planet_weight(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def mst(q):
    weight = 0
    while q:
        w, a, b = heapq.heappop(q)
        if union(a, b):
            weight += w

    return weight


N = int(sys.stdin.readline())

parent = [x for x in range(N)]
planet = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append([x, y, z, i])

queue = []

planet.sort(key=lambda x: x[0])
for i in range(1, N):
    heapq.heappush(queue, [two_planet_weight(planet[i - 1], planet[i]), planet[i-1][3], planet[i][3]])

planet.sort(key=lambda x: x[1])
for i in range(1, N):
    heapq.heappush(queue, [two_planet_weight(planet[i - 1], planet[i]), planet[i-1][3], planet[i][3]])

planet.sort(key=lambda x: x[2])
for i in range(1, N):
    heapq.heappush(queue, [two_planet_weight(planet[i - 1], planet[i]), planet[i-1][3], planet[i][3]])

print(mst(queue))
