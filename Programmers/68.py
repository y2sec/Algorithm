# 2 x N 타일링

def solution(n):
    a, b = 1, 1

    for i in range(1, n):
        a, b = b, (a+b) % 1000000007
    return b


print(solution(4))
