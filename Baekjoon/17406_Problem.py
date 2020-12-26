# 17406 배열 돌리기 4
import copy
import itertools

# 회전하는 메소드
def rotate(r, c, s, data):
    cyLst = copy.deepcopy(data)

    # 테두리부터 순서대로 회전을 진행
    while s > 0:
        sX, sY = r - s - 1, c - s - 1
        eX, eY = r + s - 1, c + s - 1

        for i in range(sX, eX + 1):
            if i == sX:
                cyLst[i][sY + 1] = data[i][sY]
            else:
                cyLst[i - 1][sY] = data[i][sY]

        for i in range(sX, eX + 1):
            if i == eX:
                cyLst[i][eY - 1] = data[i][eY]
            else:
                cyLst[i + 1][eY] = data[i][eY]

        for i in range(sY, eY + 1):
            if i == sY:
                cyLst[eX - 1][i] = data[eX][i]
            else:
                cyLst[eX][i - 1] = data[eX][i]

        for i in range(sY, eY + 1):
            if i == eY:
                cyLst[sX + 1][i] = data[sX][i]
            else:
                cyLst[sX][i + 1] = data[sX][i]
        s -= 1

    return cyLst


N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
kLst = [tuple(map(int, input().split())) for _ in range(K)]
cases = [x for x in range(K)]
result = float('inf')

# permutations를 통해 모든 경우의 수를 확인
cases = list(itertools.permutations(cases, K))

# 모든 경우의 수를 실행
for case in cases:
    clst = copy.deepcopy(lst)
    for n in case:
        clst = rotate(kLst[n][0], kLst[n][1], kLst[n][2], clst)

    for l in clst:
        result = min(result, sum(l))

print(result)
