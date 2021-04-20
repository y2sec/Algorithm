# 예상 대진표

def solution(n, a, b):
    answer = 0
    while n > 0:
        answer += 1
        a = (a - 1) // 2 + 1
        b = (b - 1) // 2 + 1

        if a == b:
            break

        n //= 2
    return answer


print(solution(8, 4, 7))
