# 미로 탈출

import collections


def bfs(cx, cy):
    global maze, visited, N, M

    queue = collections.deque()
    queue.append([cx, cy])
    visited[cx][cy] = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == '1' and visited[cx][cy] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append([nx, ny])

    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]

print(bfs(0, 0))
