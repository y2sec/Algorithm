# 7569 토마토

import collections
import sys

M, N, H = map(int, sys.stdin.readline().split())

farm = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
need_visit = collections.deque()
visited = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 1:
                need_visit.append((i, j, k, 0))


while need_visit:
    curX, curY, curZ, cnt = need_visit.popleft()
    if farm[curX][curY][curZ] == 1:
        visited[curX][curY][curZ] = cnt
        for x, y, z in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
            nxtX, nxtY, nxtZ = curX + x, curY + y, curZ + z
            if H > nxtX >= 0 and N > nxtY >= 0 and M > nxtZ >= 0 and farm[nxtX][nxtY][nxtZ] == 0:
                farm[nxtX][nxtY][nxtZ] = 1
                need_visit.append((nxtX, nxtY, nxtZ, cnt+1))

ans = 0
isAvailable = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == float('inf'):
                if farm[i][j][k] != -1:
                    isAvailable = False
                    break
            else:
                ans = max(ans, visited[i][j][k])

print(ans if isAvailable else -1)
