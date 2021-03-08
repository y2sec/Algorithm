# 자물쇠와 열쇠

import copy


def rotate(key):
    M = len(key)
    rotate_key = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotate_key[j][M-i-1] = key[i][j]

    return rotate_key


def isAvailable(key, lock, i, j):
    N, M = len(lock), len(key)

    unlock = copy.deepcopy(lock)

    for x in range(N):
        for y in range(N):
            if 0 > M+x-i-1 or M+x-i-1 >= M or 0 > M+y-j-1 or M+y-j-1 >= M:
                continue
            else:
                unlock[x][y] += key[M+x-i-1][M+y-j-1]

    for res in unlock:
        if 0 in res or 2 in res:
            return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)
    answer = False
    for _ in range(4):
        for i in range(N+M-1):
            for j in range(N+M-1):
                if isAvailable(key, lock, i, j):
                    return True
        key = rotate(key)

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
