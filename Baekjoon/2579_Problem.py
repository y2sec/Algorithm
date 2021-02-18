# 2579 계단 오르기

import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

dp[0][1] = stairs[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

print(max(dp[N-1][1:]))
