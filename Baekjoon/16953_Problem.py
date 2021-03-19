# 16953 A -> B

A, B = map(int, input().split())
cnt = 1

while A < B:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break

    cnt += 1

print(cnt if A == B else -1)
