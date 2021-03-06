# 1783 병든 나이트

N, M = map(int, input().split())

if N <= 1:
    print(1)
elif N <= 2:
    print(min((M-1) // 2 + 1, 4))
else:
    if M <= 6:
        print(min(M, 4))
    elif M <= 7:
        print(min(M, 5))
    else:
        print(5 + (M - 7))
