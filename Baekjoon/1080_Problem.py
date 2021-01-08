# 1080 행렬

N, M = map(int, input().split())
A = [[int(x) for x in input()] for _ in range(N)]
B = [[int(x) for x in input()] for _ in range(N)]

cnt = 0
# 모든 자리를 비교해가며 뒤집음
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            for x in range(3):
                for y in range(3):
                    A[i+x][j+y] = (A[i+x][j+y] + 1) % 2

# 그래도 두 행렬이 다르면 -1을 아니면 cnt를 출력
if A == B:
    print(cnt)
else:
    print(-1)
