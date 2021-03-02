# 게임 개발

N, M = map(int, input().split())
cx, cy, la = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

location = [(3, 2), (0, 3), (1, 0), (2, 1)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 1
while True:
    visited[cx][cy] = True
    move = False
    for i in range(4):
        la = location[la][0]
        nx = cx + d[la][0]
        ny = cy + d[la][1]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0 and not visited[nx][ny]:
            move = True
            cx, cy = nx, ny
            cnt += 1
            break

    if not move:
        nx = cx + d[location[la][1]][0]
        ny = cy + d[location[la][1]][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or maps[nx][ny] == 1:
            break
        cx, cy = nx, ny

print(cnt)
