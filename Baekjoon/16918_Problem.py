# 16918 봄버맨

def init():
    for x in range(R):
        for y in range(C):
            if bombMap[x][y] == 'O':
                timeMap[x][y] = 2


def checkBomb():
    for x in range(R):
        for y in range(C):
            if bombMap[x][y] == 'O' and timeMap[x][y] == 1:
                bomb(x, y)
            elif bombMap[x][y] == 'O':
                timeMap[x][y] -= 1
            else:
                if timeMap[x][y] == -second:
                    continue
                bombMap[x][y] = 'O'
                timeMap[x][y] = 3


def bomb(x, y):
    bombMap[x][y] = '.'
    timeMap[x][y] = 0

    for dx, dy in bombRange:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue

        if bombMap[nx][ny] == 'O' and timeMap[nx][ny] == 1:
            continue

        bombMap[nx][ny] = '.'
        timeMap[nx][ny] = -second


R, C, N = map(int, input().split())
bombMap = [list(input()) for _ in range(R)]
timeMap = [[0 for _ in range(C)] for _ in range(R)]

bombRange = [(0, 1), (1, 0), (0, -1), (-1, 0)]

init()

for second in range(1, N):
    checkBomb()

for bombMapLine in bombMap:
    print(''.join(bombMapLine))
