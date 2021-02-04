# 2206 벽 부수고 이동하기

import collections
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
need_visit = collections.deque()

# x, y, 벽
need_visit.append((0, 0, 0))
visited[0][0][0] = 1
while need_visit:
    x, y, wall = need_visit.popleft()

    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + i, y + j
        if N <= nx or nx < 0 or M <= ny or ny < 0:
            continue
        if maze[nx][ny] == '0' and visited[nx][ny][wall] == float('inf'):
            need_visit.append((nx, ny, wall))
            visited[nx][ny][wall] = visited[x][y][wall] + 1

        elif maze[nx][ny] == '1' and not wall:
            need_visit.append((nx, ny, 1))
            visited[nx][ny][1] = visited[x][y][0] + 1


print(min(visited[N-1][M-1]) if min(visited[N-1][M-1]) != float('inf') else -1)
