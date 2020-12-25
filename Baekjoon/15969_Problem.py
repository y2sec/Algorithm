# 15969 행복

N = int(input())
score = list(map(int, input().split()))

# 최대 점수와 최소 점수의 차를 구함
print(max(score)-min(score))
