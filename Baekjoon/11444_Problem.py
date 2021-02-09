# 11444 피보나치 수 6

import sys
sys.setrecursionlimit(10**6)


def matrixMulti(matrixA, matrixB):
    ans = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] = (ans[i][j] + (matrixA[i][k] * matrixB[k][j])) % 1000000007

    return ans


def DAC(n):
    if n == 1:
        return matrix
    if n == 2:
        return matrixMulti(matrix, matrix)

    m = DAC(n // 2)
    if n % 2 == 1:
        return matrixMulti(matrixMulti(m, m), matrix)
    return matrixMulti(m, m)


N = int(input())
matrix = [[1, 1], [1, 0]]
result = DAC(N)
print(result[0][1] % 1000000007)
