# 기둥과 보 설치

def totalInspection(n, build):
    for x in range(n + 1):
        for y in range(n + 1):
            if build[x][y][0]:
                if not (x == 0
                        or (x-1 >= 0 and build[x - 1][y][0])
                        or build[x][y][1]
                        or (y-1 >= 0 and build[x][y - 1][1])):
                    return False
            if build[x][y][1]:
                if not (x-1 >= 0 and (build[x - 1][y][0])
                        or (x-1 >= 0 and y+1 <= n and build[x - 1][y + 1][0])
                        or (y-1 >= 0 and y+1 <= n and build[x][y - 1][1] and build[x][y + 1][1])):
                    return False
    return True


def solution(n, build_frame):
    answer = []

    build = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]

    # build[y][x] == (x, y)
    for x, y, a, b in build_frame:
        # 기둥
        if a == 0:
            # 삭제
            if b == 0:
                build[y][x][0] = 0
                if not totalInspection(n, build):
                    build[y][x][0] = 1
            # 설치
            else:
                if y == 0 or build[y - 1][x][0] or build[y][x - 1][1] or build[y][x][1]:
                    build[y][x][0] = 1
        # 보
        else:
            if b == 0:
                build[y][x][1] = 0
                if not totalInspection(n, build):
                    build[y][x][1] = 1
            else:
                if build[y - 1][x][0] or (x + 1 <= n and build[y - 1][x + 1][0]) or (
                        x + 1 <= n and build[y][x - 1][1] and build[y][x + 1][1]):
                    build[y][x][1] = 1

    for i in range(n + 1):
        for j in range(n + 1):
            if build[i][j][0]:
                answer.append([j, i, 0])
            if build[i][j][1]:
                answer.append([j, i, 1])

    return answer


result = solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                      [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
print(sorted(result))
