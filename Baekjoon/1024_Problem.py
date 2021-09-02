# 1024 수열의 합

N, L = map(int, input().split())

for length in range(L, 101):
    num = N - (length * (length - 1) // 2)
    if num < 0:
        continue

    if num % length != 0:
        continue

    minNum = num // length

    for i in range(length):
        print(minNum + i, end=' ')

    exit()

print(-1)
