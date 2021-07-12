# 입국심사

def solution(n, times):
    answer = float('inf')
    times.sort()

    minTime = 0
    maxTime = 1000000000 * 1000000000
    midTime = (minTime + maxTime) // 2

    while minTime <= maxTime:
        passN = 0
        for time in times:
            passN += midTime // time

        if passN >= n:
            answer = min(answer, midTime)
            maxTime = midTime - 1
        else:
            minTime = midTime + 1

        midTime = (minTime + maxTime) // 2

    return answer


print(solution(6, [7, 10]))
