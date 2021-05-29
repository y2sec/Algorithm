# 4963 섬의 개수

import sys

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(sx, sy):
    stack = [(sx, sy)]

    while stack:
        cx, cy = stack.pop()

        for idx in range(8):
            nx, ny = cx + dx[idx], cy + dy[idx]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if not maps[nx][ny]:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            stack.append((nx, ny))

    return 1


w, h = map(int, sys.stdin.readline().split())

while w != 0 or h != 0:
    result = 0

    maps = []
    for _ in range(h):
        row = list(map(int, sys.stdin.readline().split()))
        maps.append(row)

    visited = [[0 for _ in range(w)] for _ in range(h)]

    for x in range(h):
        for y in range(w):
            if not maps[x][y] or visited[x][y]:
                continue

            visited[x][y] = 1
            result += dfs(x, y)

    print(result)
    w, h = map(int, sys.stdin.readline().split())
