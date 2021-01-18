# 12865 평범한 배낭

N, K = map(int, input().split())

obj = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for __ in range(N+1)]

# 최대 무게에서 현재 물건을 뺀 무게에 최대 가치에 현재 물건의 가치를 더한 값과 현재 물건을 빼지 않은 최대 가치의 값의 최대 값을 dp에 저장
for i in range(1, N+1):
    for j in range(1, K+1):
        if obj[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-obj[i-1][0]] + obj[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
