# 2164 카드2

import collections

N = int(input())
queue = collections.deque()

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())
