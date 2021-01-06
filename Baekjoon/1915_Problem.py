# 1915 가장 큰 정사각형

N, M = map(int, input().split())
lst = [[int(x) for x in input()] for _ in range(N)]
DP = [[0 for __ in range(M+1)] for _ in range(N+1)]

result = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if lst[i-1][j-1]:
            DP[i][j] = min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j]) + 1
            result = max(DP[i][j], result)

print(result**2)
