# 1629 곱셈

import sys
sys.setrecursionlimit(10**6)


def mulit(b):
    global ans
    if b == 1:
        return A % C
    if b == 2:
        return (A ** 2) % C

    if b % 2 == 1:
        return (mulit(b//2) ** 2 * A) % C
    return (mulit(b//2) ** 2) % C


A, B, C = map(int, input().split())
ans = A
print(mulit(B))
