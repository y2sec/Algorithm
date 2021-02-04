# 2667 단지번호붙이기

def bfs(x, y):
    if graph[x][y] == 0 or visited[x][y]:
        return 0
    cnt = 0
    need_visit = [(x, y)]

    while need_visit:
        curX, curY = need_visit.pop(0)
        if N > curX >= 0 and N > curY >= 0 and graph[curX][curY] and not visited[curX][curY]:
            visited[curX][curY] = True
            cnt += 1
            for nxtX, nxtY in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                need_visit.append((curX + nxtX, curY + nxtY))

    return cnt


N = int(input())
graph = [[int(x) for x in input()] for _ in range(N)]
visited = [[False for x in range(N)] for _ in range(N)]


complexHouse = []

for i in range(N):
    for j in range(N):
        house = 0
        complexNum = bfs(i, j)
        if complexNum:
            complexHouse.append(complexNum)

complexHouse.sort()
print(len(complexHouse))
for cn in complexHouse:
    print(cn)
