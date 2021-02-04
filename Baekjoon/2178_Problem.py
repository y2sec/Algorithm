# 2178 미로 탐색

def bfs(x, y):
    visited = [[float('inf') for _ in range(M)] for _ in range(N)]
    need_visit = [(x, y, 1)]
    while need_visit:
        curX, curY, cnt = need_visit.pop(0)

        if N > curX >= 0 and M > curY >= 0 and maze[curX][curY]and cnt < visited[curX][curY]:
            visited[curX][curY] = cnt
            for nxtX, nxtY in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                need_visit.append((curX+nxtX, curY+nxtY, cnt+1))

    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [[int(x) for x in input()] for _ in range(N)]
print(bfs(0, 0))
