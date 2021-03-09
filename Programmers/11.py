# 외벽 점검

import itertools


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(n+weak[i])

    for start in range(length):
        for friends in itertools.permutations(dist, len(dist)):
            cnt = 1
            position = weak[start] + friends[cnt-1]
            for index in range(start, start+length):
                if position < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer


solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
