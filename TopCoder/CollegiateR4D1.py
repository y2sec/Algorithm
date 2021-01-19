# CollegiateR4D1 ChessMetric

def dfs(x, y, moves):
    if x < 0 or x >= size or y < 0 or y >= size:
        return 0

    if moves == numMoves:
        if (x, y) == end:
            return 1
        else:
            return 0
    cnt = 0
    for nx, ny in move:
        cnt += dfs(x + nx, y + ny, moves + 1)
    return cnt


def dp():
    dpLst = [[[0 for _ in range(numMoves+1)] for __ in range(size)] for ___ in range(size)]
    dpLst[start[0]][start[1]][0] = 1
    for i in range(1, numMoves+1):
        for x in range(size):
            for y in range(size):
                for nx, ny in move:
                    if x+nx < 0 or x+nx >= size or y+ny < 0 or y+ny >= size:
                        continue
                    dpLst[x+nx][y+ny][i] += dpLst[x][y][i-1]

    print(dpLst[end[0]][end[1]][numMoves])


move = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (-2, -1), (-2, 1), (-1, -2), (1, -2),
        (2, -1), (2, 1), (-1, 2), (1, 2)]
size = 100
start = (0, 0)
end = (0, 99)
numMoves = 50
# ans = dfs(start[0], start[1], 0)
# print(ans)
dp()
