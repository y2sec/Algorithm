# 11047 동전 0

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
ans = 0

for i in range(N-1, -1, -1):
    n = K // coin[i]
    if n > 0:
        K -= (n * coin[i])
        ans += n

    if K == 0:
        break

print(ans)
