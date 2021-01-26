# 1018 체스판 다시 칠하기

def chkChess(start, x, y):
    cnt = 0

    for i in range(x, x+8):
        for j in range(y, y+8):
            if chess[i][j] != start:
                cnt += 1

            if start == 'B':
                start = 'W'
            else:
                start = 'B'
        if start == 'B':
            start = 'W'
        else:
            start = 'B'

    return cnt


N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

ans = N * M

for i in range(N-8+1):
    for j in range(M-8+1):
        ans = min(ans, chkChess('B', i, j), chkChess('W', i, j))

print(ans)
