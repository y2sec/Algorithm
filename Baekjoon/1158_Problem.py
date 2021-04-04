# 1158 요세푸스 문제

N, K = map(int, input().split())

circle = [idx for idx in range(1, N+1)]

cnt = 0

print('<', end='')
while circle:
    cnt = (cnt + K-1) % len(circle)
    if len(circle) == 1:
        print(circle.pop(cnt), end='>')
    else:
        print(circle.pop(cnt), end=', ')
