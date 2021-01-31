# 10773 제로

import sys

K = int(input())

stack = []

for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
