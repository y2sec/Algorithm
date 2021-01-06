# 2167 2차원 배열의 합

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
tc = int(input())
result_lst = []

# 일반적으로 해당 값을 더한 후 출력
for _ in range(tc):
    i, j, x, y = map(int, input().split())
    result = 0
    data = lst[i - 1:x]
    for d in data:
        result += sum(d[j - 1:y])

    result_lst.append(result)

for result in result_lst:
    print(result)

# 누적 합을 이용한 알고리즘

DP = [[0 for _ in range(M+1)] for __ in range(N+1)]

# DP[i][j] = 바로 위 누적합 + 바로 옆 누적합 - 교집합인 대각선 누적합 + (i,j) 위치 값
for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = lst[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

# (i,j) 부터 (x,y)의 값 = (x,y) - (i-1,y) - (x,j-1) + (i-1,j-1)
for _ in range(tc):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])
