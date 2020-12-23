# 12100 2048(Easy)

# rotate를 통해 개선 시킬 수 있음
# 90도씩 돌려가면서 한 쪽으로만 푸쉬
import copy

# 위치를 이동시키기 위한 메소드
def sort(cur, blocks):
    for i in range(N):
        if cur == 'N':
            for x in range(N):
                if blocks[x][i] == 0:
                    for y in range(x + 1, N):
                        if blocks[y][i] != 0:
                            blocks[x][i], blocks[y][i] = blocks[y][i], blocks[x][i]
                            break
        elif cur == 'S':
            for x in range(N - 1, -1, -1):
                if blocks[x][i] == 0:
                    for y in range(x - 1, -1, -1):
                        if blocks[y][i] != 0:
                            blocks[x][i], blocks[y][i] = blocks[y][i], blocks[x][i]
                            break
        elif cur == 'W':
            for x in range(N):
                if blocks[i][x] == 0:
                    for y in range(x + 1, N):
                        if blocks[i][y] != 0:
                            blocks[i][x], blocks[i][y] = blocks[i][y], blocks[i][x]
                            break
        elif cur == 'E':
            for x in range(N - 1, -1, -1):
                if blocks[i][x] == 0:
                    for y in range(x - 1, -1, -1):
                        if blocks[i][y] != 0:
                            blocks[i][x], blocks[i][y] = blocks[i][y], blocks[i][x]
                            break


# 같은 수를 만났을때 두 수를 더하는 메소드
def DFS(n, cur, blocks):
    global result
    result = max(result, max([max(b) for b in blocks]))
    if n == 5:
        return
    else:
        for i in range(N):
            if cur == 'N':
                for x in range(N):
                    if blocks[x][i] == 0:
                        continue
                    for y in range(x + 1, N):
                        if blocks[y][i] != 0 and blocks[y][i] == blocks[x][i]:
                            blocks[y][i] = 0
                            blocks[x][i] *= 2
                            break
                        elif blocks[y][i] != 0 and blocks[y][i] != blocks[x][i]:
                            break
            elif cur == 'S':
                for x in range(N - 1, -1, -1):
                    if blocks[x][i] == 0:
                        continue
                    for y in range(x - 1, -1, -1):
                        if blocks[y][i] != 0 and blocks[y][i] == blocks[x][i]:
                            blocks[y][i] = 0
                            blocks[x][i] *= 2
                            break
                        elif blocks[y][i] != 0 and blocks[y][i] != blocks[x][i]:
                            break
            elif cur == 'W':
                for x in range(N):
                    if blocks[i][x] == 0:
                        continue
                    for y in range(x + 1, N):
                        if blocks[i][y] != 0 and blocks[i][y] == blocks[i][x]:
                            blocks[i][y] = 0
                            blocks[i][x] *= 2
                            break
                        elif blocks[i][y] != 0 and blocks[i][y] != blocks[i][x]:
                            break
            elif cur == 'E':
                for x in range(N - 1, -1, -1):
                    if blocks[i][x] == 0:
                        continue
                    for y in range(x - 1, -1, -1):
                        if blocks[i][y] != 0 and blocks[i][y] == blocks[i][x]:
                            blocks[i][y] = 0
                            blocks[i][x] *= 2
                            break
                        elif blocks[i][y] != 0 and blocks[i][y] != blocks[i][x]:
                            break
        sort(cur, blocks)
        for nnxt in ['N', 'S', 'W', 'E']:
            DFS(n + 1, nnxt, copy.deepcopy(blocks))


N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]

result = 0
for nxt in ['N', 'S', 'W', 'E']:
    DFS(0, nxt, copy.deepcopy(block))
print(result)
