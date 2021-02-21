# 1912 연속합

N = int(input())
lst = list(map(int, input().split()))

dp = [-1001 for _ in range(N)]
dp[0] = lst[0]
for i in range(1, N):
    dp[i] = max(lst[i], dp[i-1] + lst[i])

print(max(dp))
