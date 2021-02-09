# 2630 색종이 만들기

import sys


def chk(x, y, n):
    standard = colorPaper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if colorPaper[i][j] != standard:
                return False

    return True


def cutting(x, y, n):
    global white, blue
    if n < 1:
        return
    if chk(x, y, n):
        if colorPaper[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    cutting(x, y, n//2)
    cutting(x, y+(n//2), n//2)
    cutting(x+(n//2), y, n//2)
    cutting(x+(n//2), y+(n//2), n//2)


N = int(sys.stdin.readline())
colorPaper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0
cutting(0, 0, N)

print(white)
print(blue)
