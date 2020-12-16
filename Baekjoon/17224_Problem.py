# 17224 APC는 왜 서브태스크 대회가 되었을까?


N, L, K = map(int, input().split())
result = 0
easy, hard = 0, 0

# 어려운 문제를 풀 수 있다면 hard를 아니면 easy를 1 더해줌
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    if L >= sub2:
        hard += 1
    elif L >= sub1:
        easy += 1

# 점수 계산 방식으로 점수를 계산
# 최고 점수를 받기 위해 어려운 문제 우선으로 계산
for _ in range(K):
    if hard > 0:
        result += 140
        hard -= 1
    elif easy > 0:
        result += 100
        easy -= 1

print(result)
