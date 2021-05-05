# 징검다리 건너기

def solution(stones, k):
    answer = 0
    minV = 0
    maxV = max(stones)
    midV = (maxV + minV) // 2

    while minV <= maxV:
        result = True
        cnt = 0
        for i in range(len(stones)):
            if midV > stones[i]:
                cnt += 1
            else:
                if cnt >= k:
                    result = False
                    break
                cnt = 0

        if cnt >= k:
            result = False

        if result:
            minV = midV + 1
            answer = midV
        else:
            maxV = midV - 1
        midV = (maxV + minV) // 2

    return answer
