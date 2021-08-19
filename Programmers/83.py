# 최고의 집합

def solution(n, s):
    num = s // n

    if num < 1:
        return [-1]

    answer = [num for _ in range(n)]
    remain = s % n
    for idx in range(remain):
        answer[idx] += 1

    answer.sort()
    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))