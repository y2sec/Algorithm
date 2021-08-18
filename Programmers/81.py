# 멀리 뛰기

def solution(n):
    answer = 0
    square = [0 for _ in range(n+1)]
    square[0] = 1
    square[1] = 1

    for curr in range(2, n+1):
        square[curr] = (square[curr-1] + square[curr-2]) % 1234567

    return square[n]


print(solution(4))
print(solution(3))
