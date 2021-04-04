# 2212 센서

N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
    exit()

sensorsLeng = [sensors[idx] - sensors[idx-1] for idx in range(1, N)]
sensorsLeng.sort()

for i in range(1, K):
    sensorsLeng[-i] = 0

print(sum(sensorsLeng))
