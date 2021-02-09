# 10830 행렬 제곱

import sys
sys.setrecursionlimit(10**6)


def matrixMulti(matrixA, matrixB):
    ans = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] = (ans[i][j] + (matrixA[i][k] * matrixB[k][j])) % 1000

    return ans


def DAC(b):
    if b == 1:
        return matrix
    if b == 2:
        return matrixMulti(matrix, matrix)

    m = DAC(b // 2)
    if b % 2 == 1:
        return matrixMulti(matrixMulti(m, m), matrix)
    return matrixMulti(m, m)


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = DAC(B)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=' ')
    print()
