# 11866 요세푸스 문제0

import collections

N, K = map(int, input().split())
queue = collections.deque()

for i in range(1, N+1):
    queue.append(i)

res = []

while queue:
    for i in range(K):
        if i == K-1:
            res.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print('<', end='')
for i in range(N):
    if i == N-1:
        print(res[i], end='')
    else:
        print(res[i], end=', ')
print('>')
