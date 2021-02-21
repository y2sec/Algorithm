# 11054 가장 긴 바이토닉 부분 수열

N = int(input())
seq = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        cnt = 0
        if j > i:
            for k in range(i, j):
                if seq[k] > seq[j]:
                    cnt = max(cnt, dp[i][k])
        else:
            for k in range(j):
                if seq[k] < seq[j]:
                    cnt = max(cnt, dp[i][k])
        dp[i][j] = cnt+1

res = max([max(p) for p in dp])
print(res)
