# 볼링공 고르기

N, M = map(int, input().split())
balling = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if balling[i] != balling[j]:
            cnt += 1

print(cnt)
