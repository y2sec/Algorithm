# 2004TCCCR4D1 BadNeighbors


# donations = [10, 3, 2, 5, 7, 8]
# donations = [11, 15]
donations = [7, 7, 7, 7, 7, 7, 7]
# donations = [1, 2, 3, 4, 5, 1, 2, 3 ,4 ,5]


ans = 0
dp = [[0 for _ in range(len(donations)+2)] for __ in range(len(donations)+2)]

for i in range(2, len(donations)+1):
    dp[i][i-2] = dp[i-2][i-2]
    dp[i][i-3] = dp[i-1][i-3]
    dp[i][i] = max(dp[i][:i-1]) + donations[i-2]
    ans = max(ans, dp[i][i])

dp = [[0 for _ in range(len(donations)+2)] for __ in range(len(donations)+2)]

for i in range(3, len(donations)+2):
    dp[i][i-2] = dp[i-2][i-2]
    dp[i][i-3] = dp[i-1][i-3]
    dp[i][i] = max(dp[i][:i-1]) + donations[i-2]
    ans = max(ans, dp[i][i])
for i in dp:
    print(i)


print(ans)
