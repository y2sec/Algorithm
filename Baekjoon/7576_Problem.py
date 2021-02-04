# 7576 토마토

import collections
import sys

M, N = map(int, sys.stdin.readline().split())

farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
need_visit = collections.deque()
visited = [[float('inf') for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            need_visit.append((i, j, 0))


while need_visit:
    curX, curY, cnt = need_visit.popleft()
    if farm[curX][curY] == 1:
        visited[curX][curY] = cnt
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxtX, nxtY = curX + x, curY + y
            if N > nxtX >= 0 and M > nxtY >= 0 and farm[nxtX][nxtY] == 0:
                farm[nxtX][nxtY] = 1
                need_visit.append((nxtX, nxtY, cnt+1))

ans = 0
isAvailable = True

for i in range(N):
    for j in range(M):
        if visited[i][j] == float('inf'):
            if farm[i][j] != -1:
                isAvailable = False
                break
        else:
            ans = max(ans, visited[i][j])
    if not isAvailable:
        break

print(ans if isAvailable else -1)
