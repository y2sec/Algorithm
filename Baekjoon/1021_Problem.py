# 1021 회전하는 큐

import collections

N, M = map(int, input().split())

deque = collections.deque()
for i in range(1, N+1):
    deque.append(i)

lst = list(map(int, input().split()))
ans = 0

for x in lst:
    if deque[0] == x:
        deque.popleft()
    else:
        idx = deque.index(x)
        if idx < len(deque)-idx:
            for i in range(idx):
                deque.append(deque.popleft())
            ans += idx
        else:
            for i in range(len(deque)-idx):
                deque.appendleft(deque.pop())
            ans += (len(deque) - idx)
        deque.popleft()

print(ans)
