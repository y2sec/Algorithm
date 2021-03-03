# 2839 설탕 배달

N = int(input())

res = 0

while N >= 3:
    if N % 5 == 0:
        break
    res += 1
    N -= 3

if N % 5 == 0:
    res += (N // 5)
    print(res)
else:
    print(-1)
