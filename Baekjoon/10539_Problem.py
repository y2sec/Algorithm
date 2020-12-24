# 10539 수빈이와 수열

N = int(input())
num = list(map(int, input().split()))
result = list()

# 수열을 구함
for i in range(1, N+1):
    result.append(num[i-1] * i)
    for j in range(1, i):
        result[i-1] -= result[j-1]

# 수열 출력
[print(n, end=' ') for n in result]
