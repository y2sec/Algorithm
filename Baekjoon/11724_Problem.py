# 11724 연결 요소의 개수
import sys


def bfs(start):
    queue = [start]
    while queue:
        current = queue.pop(0)

        for nxt in linked[current]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            queue.append(nxt)

    return 1


N, M = map(int, sys.stdin.readline().split())
result = 0
linked = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    linked[u].append(v)
    linked[v].append(u)

visited = [0 for _ in range(N + 1)]

for vertex in range(1, N + 1):
    if visited[vertex]:
        continue

    result += bfs(vertex)

print(result)
