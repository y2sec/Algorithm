# 9372 상근이의 여행

import sys


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
    else:
        parent[A] = B
        return True


def st(n, m, lst):
    cnt = 0

    for a, b in lst:
        if union(a, b):
            cnt += 1

    return cnt


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    route = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    parent = [x for x in range(N + 1)]
    print(st(N, M, route))
