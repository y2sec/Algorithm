# 1300 K번째 수

N = int(input())
K = int(input())

minV = 1
maxV = N * N
midV = (minV + maxV) // 2

ans = N * N
while minV <= maxV:
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, midV // i)
    print(midV, cnt)
    if cnt >= K:
        ans = min(ans, midV)
        maxV = midV - 1
    elif cnt < K:
        minV = midV + 1
    midV = (minV + maxV) // 2

print(ans)
