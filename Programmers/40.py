# 점프와 순간 이동

def solution(n):
    answer = 0

    while n > 0:
        if n % 2 == 1:
            n -= 1
            answer += 1
            continue
        n //= 2

    return answer
