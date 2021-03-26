# 1697 숨바꼭질

from collections import deque


def BFS():
    q = deque([N])
    visit = [0] * 100001
    while q:
        node = q.popleft()
        if node == K:
            return visit[node]

        if node + 1 <= 100000 and not visit[node + 1]:
            q.append(node + 1)
            visit[node + 1] = visit[node] + 1
        if node - 1 >= 0 and not visit[node - 1]:
            q.append(node - 1)
            visit[node - 1] = visit[node] + 1
        if node * 2 <= 100000 and not visit[node * 2]:
            q.append(node * 2)
            visit[node * 2] = visit[node] + 1


N, K = map(int, input().split())

print(BFS())
