# 2447 별 찍기 - 10

def star(n, x, y):
    if n // 3 == 1:
        for i in range(x, x + n):
            for j in range(y, y + n):
                if i == x + 1 and j == y + 1:
                    continue
                maps[i][j] = '*'

        return

    nxtN = n // 3
    star(nxtN, x, y)
    star(nxtN, x, y + nxtN)
    star(nxtN, x, y + (nxtN * 2))
    star(nxtN, x + nxtN, y)
    star(nxtN, x + nxtN, y + (nxtN * 2))
    star(nxtN, x + (nxtN * 2), y)
    star(nxtN, x + (nxtN * 2), y + nxtN)
    star(nxtN, x + (nxtN * 2), y + (nxtN * 2))


N = int(input())

maps = [[' ' for _ in range(N)] for _ in range(N)]
star(N, 0, 0)

for m in maps:
    print(''.join(m))
