# 3190 뱀

import sys
import collections

N = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())
moves = collections.deque()
for _ in range(L):
    x, c = sys.stdin.readline().split()
    moves.append([int(x), c])

queue = collections.deque()
queue.append((0, 0))

move = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sec = 0

px = 0
isAvailable = True
while isAvailable:

    if moves:
        X, C = moves.popleft()
    else:
        X, C = 10**10, 'D'
    for i in range(px, X):
        sec += 1
        cx, cy = queue[-1]
        nx, ny = cx + dx[move], cy + dy[move]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            isAvailable = False
            break
        elif (nx, ny) in queue:
            isAvailable = False
            break
        else:
            queue.append((nx, ny))

        if board[nx][ny] == 1:
            board[nx][ny] = 0
            K -= 1
        else:
            queue.popleft()

    px = X
    if C == 'D':
        move = (move + 1) % 4
    else:
        move -= 1
        if move == -1:
            move = 3

print(sec)
