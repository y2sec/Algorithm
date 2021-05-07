# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []

    matrix = [[((i - 1) * columns + j) for j in range(1, columns + 1)] for i in range(1, rows + 1)]

    def rotate(sx, sy, ex, ey):
        copyMatrix = [[matrix[x+sx][y+sy] for y in range(ey-sy+1)] for x in range(ex-sx+1)]
        minV = matrix[sx][sy]

        for x in range(sx + 1, ex + 1):
            matrix[x][ey] = copyMatrix[x-1-sx][ey-sy]
            minV = min(minV, matrix[x][ey])

        for y in range(sy, ey):
            matrix[ex][y] = copyMatrix[ex-sx][y+1-sy]
            minV = min(minV, matrix[ex][y])

        for x in range(sx, ex):
            matrix[x][sy] = copyMatrix[x+1-sx][0]
            minV = min(minV, matrix[x][sy])

        for y in range(sy + 1, ey + 1):
            matrix[sx][y] = copyMatrix[0][y-1-sy]
            minV = min(minV, matrix[sx][y])

        return minV

    for sx, sy, ex, ey in queries:
        answer.append(rotate(sx - 1, sy - 1, ex - 1, ey - 1))

    return answer
