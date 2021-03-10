# 카펫

import math


def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for i in range(int(math.sqrt(total)), total + 1):
        if total % i != 0:
            continue
        row = i
        col = total // i
        if row < col:
            continue

        if brown == row * 2 + (col - 2) * 2:
            answer = [row, col]
            break

    return answer