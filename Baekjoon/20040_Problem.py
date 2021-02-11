# 20040 사이클 게임

import sys

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

    parent[B] = A
    return True


N, M = map(int, sys.stdin.readline().split())
parent = [x for x in range(N)]
ans = 0
for i in range(1, M+1):
    A, B = map(int, sys.stdin.readline().split())
    if not ans and not union(A, B):
        ans = i

print(ans)
