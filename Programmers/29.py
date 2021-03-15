# 게임 맵 최단거리

def solution(maps):
    def bfs():
        queue = [[0, 0, 1]]
        row, col = len(maps[0]), len(maps)
        visited = [[0 for _ in range(row)] for _ in range(col)]
        visited[0][0] = 1

        while queue:
            x, y, cnt = queue.pop(0)

            if x == col - 1 and y == row - 1:
                return cnt

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 > nx or nx >= col or 0 > ny or ny >= row:
                    continue
                if maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny, cnt + 1])

        return -1
    return bfs()
