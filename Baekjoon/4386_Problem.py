# 4386 별자리 만들기

import math
import sys
import heapq


def find(a):
    global parent
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    global parent
    A = find(a)
    B = find(b)

    if A == B:
        return False
    parent[A] = B
    return True


def two_stars_length(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def mst(q):
    weight = 0
    while q:
        w, a, b = heapq.heappop(q)
        if union(a, b):
            weight += w

    return weight


N = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]
queue = []
for i in range(N):
    for j in range(i + 1, N):
        heapq.heappush(queue, [two_stars_length(stars[i], stars[j]), i, j])

parent = [x for x in range(N)]
print('%.2f' % mst(queue))
