# 스티커 모으기(2)

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    size = len(sticker)
    sticker = sticker * 2

    answer = 0
    for i in range(3):
        pick = [0 for _ in range(size-1)]
        pick[0], pick[1] = sticker[i], sticker[i]

        maxSum = pick[0]
        for j in range(2, size-1):
            pick[j] = maxSum + sticker[j + i]
            maxSum = max(maxSum, pick[j - 1])

        answer = max(answer, max(pick))

    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
print(solution([1]))
print(solution([1, 2]))
