# 경주로 건설

import collections


def solution(board):
    answer = 0
    N = len(board)

    def bfs(x, y):
        queue = collections.deque()
        visited = [[float('inf') for _ in range(N)] for _ in range(N)]
        queue.append([x, y, 0, 'x'])
        visited[x][y] = 0
        rowV, colV = 100, 100

        while queue:
            cx, cy, value, direction = queue.popleft()
            if direction == 'r':
                rowV, colV = 100, 600
            elif direction == 'c':
                rowV, colV = 600, 100
            else:
                rowV, colV = 100, 100

            for dx, dy in [[0, 1], [0, -1]]:
                nx, ny = cx + dx, cy + dy
                nV = value + rowV
                if nx >= N or ny >= N or nx < 0 or ny < 0:
                    continue

                if board[nx][ny] or visited[nx][ny] < nV:
                    continue
                visited[nx][ny] = nV
                queue.append([nx, ny, nV, 'r'])

            for dx, dy in [[1, 0], [-1, 0]]:
                nx, ny = cx + dx, cy + dy
                nV = value + colV
                if nx >= N or ny >= N or nx < 0 or ny < 0:
                    continue

                if board[nx][ny] or visited[nx][ny] < nV:
                    continue
                visited[nx][ny] = nV
                queue.append([nx, ny, nV, 'c'])

        return visited[N-1][N-1]

    return bfs(0, 0)
