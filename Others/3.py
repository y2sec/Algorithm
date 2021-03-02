# 음료수 얼려 먹기

import collections


def bfs(cx, cy):
    global ice_basket, visited
    queue = collections.deque()
    queue.append([cx, cy])
    visited[cx][cy] = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M and ice_basket[nx][ny] == '0' and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1

    return 1


N, M = map(int, input().split())
ice_basket = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
for x in range(N):
    for y in range(M):
        if not visited[x][y] and ice_basket[x][y] == '0':
            cnt += bfs(x, y)

print(cnt)
