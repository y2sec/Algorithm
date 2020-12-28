# 11055 가장 큰 증가 부분 수열

N = int(input())
A = list(map(int, input().split()))

DP = [0 for _ in range(N)]

# 이전 값들을 탐색하면서 자기보다 작은 수 중 가장 큰 DP값을 저장해 자신의 값과 더해줌
for i in range(N):
    value = 0
    for j in range(i):
        if A[i] > A[j]:
            value = max(value, DP[j])
    DP[i] = value + A[i]

print(max(DP))
