# 7562 나이트의 이동

import sys
import collections


def bfs(l, sx, sy, ex, ey):
    chess = [[float('inf')] * l for _ in range(l)]
    queue = collections.deque()
    queue.append([sx, sy])
    chess[sx][sy] = 0
    while queue:
        cx, cy = queue.popleft()

        if (cx, cy) == (ex, ey):
            return chess[cx][cy]

        for dx, dy in [[-2, -1],[-2, 1],[2, -1],[2, 1],[1, -2],[-1, -2],[1, 2],[-1, 2]]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if (nx, ny) == (ex, ey):
                return chess[cx][cy] + 1
            if chess[nx][ny] > chess[cx][cy] + 1:
                chess[nx][ny] = chess[cx][cy] + 1
                queue.append([nx, ny])
    return chess[ex][ey]


T = int(sys.stdin.readline())
for _ in range(T):
    l = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    print(bfs(l, sx, sy, ex, ey))
