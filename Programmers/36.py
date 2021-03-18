# 블록 이동하기

import heapq


def union(A, B, parent):
    A = find(A, parent)
    B = find(B, parent)

    if A == B:
        return False
    parent[A] = B
    return True


def find(A, parent):
    if parent[A] == A:
        return A
    parent[A] = find(parent[A], parent)

    return parent[A]


def solution(n, costs):
    heap = []

    for cost in costs:
        heapq.heappush(heap, [cost[2], cost[0], cost[1]])

    def mst():
        sum_weight = 0
        parent = [x for x in range(n + 1)]
        while heap:
            weight, islandA, islandB = heapq.heappop(heap)
            if union(islandA, islandB, parent):
                sum_weight += weight

        return sum_weight

    return mst()


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
