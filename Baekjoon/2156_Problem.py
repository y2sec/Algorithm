# 2156 포도주 시식

import sys

N = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0][1] = wine[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[N-1]))
