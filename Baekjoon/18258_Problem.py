# 18258 큐 2

import sys
import collections

N = int(sys.stdin.readline())
queue = collections.deque()

for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push':
        queue.append(operation[1])
    elif operation[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif operation[0] == 'size':
        print(len(queue))
    elif operation[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif operation[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif operation[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
