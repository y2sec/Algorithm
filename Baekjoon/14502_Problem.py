# 14502 연구소

def build(f, s, t):
    safety = 0

    for idx in [f, s, t]:
        room[idx // M][idx % M] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if room[x][y] != 2:
                continue
            bfs(x, y, visited)

    for x in range(N):
        for y in range(M):
            if room[x][y] == 0 and not visited[x][y]:
                safety += 1

    for idx in [f, s, t]:
        room[idx // M][idx % M] = 0

    return safety


def bfs(x, y, visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited[x][y] = True

    queue = [(x, y)]

    while queue:
        cx, cy = queue.pop(0)

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if room[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))


N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N * M):
    if room[i // M][i % M]:
        continue

    for j in range(i + 1, N * M):
        if room[j // M][j % M]:
            continue

        for k in range(j + 1, N * M):
            if room[k // M][k % M]:
                continue

            result = max(result, build(i, j, k))

print(result)
