# 기지국 설치
import math


def solution(n, stations, w):
    answer = 0

    stations.sort()

    curr = 0
    while curr <= n:
        if not stations:
            answer += math.ceil((n - curr + 1) / (w * 2 + 1))
            break

        nxt = stations.pop(0)
        if nxt - w > curr:
            answer += math.ceil((nxt - w - curr) / (w * 2 + 1))

        curr = nxt + w + 1

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
