# 2565 전깃줄

N = int(input())
eline = [tuple(map(int, input().split())) for _ in range(N)]
eline.sort()

dp = [0 for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(i):
        if eline[i][0] > eline[j][0] and eline[i][1] < eline[j][1]:
            continue
        elif eline[i][0] < eline[j][0] and eline[i][1] > eline[j][1]:
            continue
        else:
            cnt = max(cnt, dp[j])
    dp[i] = cnt+1

print(N - max(dp))
