# 1992 쿼드트리

import sys


def chk(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[x][y] != video[i][j]:
                return False

    return True


def zipVideo(x, y, n):
    if n < 1:
        return
    if chk(x, y, n):
        print(video[x][y], end='')
        return
    print('(', end='')
    zipVideo(x, y, n//2)
    zipVideo(x, y + (n // 2), n // 2)
    zipVideo(x+(n//2), y, n//2)
    zipVideo(x+(n//2), y+(n//2), n//2)
    print(')', end='')


N = int(sys.stdin.readline())
video = [list(sys.stdin.readline().strip()) for _ in range(N)]
zipVideo(0, 0, N)
