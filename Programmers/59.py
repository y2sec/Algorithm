# 동굴 탐험

import collections


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for parent, child in path:
        graph[parent].append(child)
        graph[child].append(parent)

    before = [0] * n
    after = [-1] * n

    for f, s in order:
        before[s] = f

    if before[0] != 0:
        return False

    queue = collections.deque()
    queue.extend(graph[0])
    visited = [0 for _ in range(n)]
    visited[0] = 1

    while queue:
        cur = queue.popleft()
        if visited[cur]:
            continue

        if not visited[before[cur]]:
            after[before[cur]] = cur
            continue

        visited[cur] = 1
        for nxt in graph[cur]:
            queue.append(nxt)

        if after[cur] != -1:
            queue.append(after[cur])

    if visited.count(0) > 0:
        return False
    return True
