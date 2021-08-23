# 줄 서는 방법
import math
answer = []


def solution(n, k):
    findLine(n, k, [i for i in range(1, n + 1)])
    return answer


def findLine(n, k, people):
    if len(people) == 0:
        return
    lineN = math.factorial(n-1)

    idx = 0
    while 0 < lineN < k:
        k -= lineN
        idx += 1

    answer.append(people.pop(idx))
    findLine(n - 1, k, people)


print(solution(3, 5))
print(solution(10, 300))
