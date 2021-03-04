# 실패율

def solution(N, stages):
    answer = []
    stages.sort(reverse=True)

    success = [0 for _ in range(N+2)]
    fail = [0 for _ in range(N+2)]

    for stage in stages:
        fail[stage] += 1
        success[stage-1] += 1

    for i in range(N-1, -1, -1):
        success[i] += success[i+1]

    failRates = []

    for i in range(1, N+1):
        p = fail[i] + success[i]
        if p == 0:
            failRates.append([0, i])
        else:
            failRates.append([fail[i] / p, i])

    failRates.sort(key=lambda x: x[0], reverse=True)

    for rate in failRates:
        answer.append(rate[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
