# 10866 덱

import collections
import sys

deque = collections.deque()
N = int(sys.stdin.readline())
for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push_back':
        deque.append(operation[1])
    elif operation[0] == 'push_front':
        deque.appendleft(operation[1])
    elif operation[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif operation[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif operation[0] == 'size':
        print(len(deque))
    elif operation[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif operation[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif operation[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
