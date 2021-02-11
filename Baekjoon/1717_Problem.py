# 1717 집합의 표현

import sys


def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    parentA = find(a)
    parentB = find(b)

    parent[parentB] = parentA


N, M = map(int, sys.stdin.readline().split())
parent = [x for x in range(N+1)]
for _ in range(M):
    oper, A, B = map(int, sys.stdin.readline().split())

    if oper:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)
