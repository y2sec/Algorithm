# 1463 1로 만들기

import collections

N = int(input())
queue = collections.deque()
queue.append([N, 0])
numbers = [float('inf') for _ in range(1000001)]
numbers[N] = 0
while queue:
    n, cnt = queue.popleft()

    if n == 1:
        print(cnt)
        break

    if cnt > numbers[n]:
        continue

    if n % 3 == 0 and cnt+1 < numbers[n//3]:
        numbers[n//3] = cnt+1
        queue.append([n//3, cnt+1])
    if n % 2 == 0 and cnt+1 < numbers[n//2]:
        numbers[n//2] = cnt+1
        queue.append([n//2, cnt+1])
    if cnt+1 < numbers[n-1]:
        numbers[n-1] = cnt+1
        queue.append([n-1, cnt+1])
