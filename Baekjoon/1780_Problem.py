# 1780 종이의 개수

import sys


def chk(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False

    return True


def cutting(x, y, n):
    global a, b, c
    if n < 1:
        return
    if chk(x, y, n):
        if paper[x][y] == -1:
            a += 1
        elif paper[x][y] == 0:
            b += 1
        else:
            c += 1
        return

    cutting(x, y, n//3)
    cutting(x, y+(n//3), n//3)
    cutting(x, y+(n//3*2), n//3)
    cutting(x+(n//3), y, n//3)
    cutting(x+(n//3), y+(n//3), n//3)
    cutting(x+(n//3), y+(n//3*2), n//3)
    cutting(x+(n//3*2), y, n//3)
    cutting(x+(n//3*2), y+(n//3), n//3)
    cutting(x+(n//3*2), y+(n//3*2), n//3)


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a, b, c = 0, 0, 0
cutting(0, 0, N)
print(a)
print(b)
print(c)
