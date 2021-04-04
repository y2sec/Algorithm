# 2357 최솟값과 최댓값

import sys

stMax = [0 for _ in range(500001)]
stMin = [float('inf') for _ in range(500001)]


def initMax(index, start, end):
    if start == end:
        stMax[index] = lst[start]
    else:
        mid = (start+end) // 2
        stMax[index] = max(initMax(index * 2+1, start, mid), initMax(index * 2+2, mid+1, end))
    return stMax[index]


def initMin(index, start, end):
    if start == end:
        stMin[index] = lst[start]
    else:
        mid = (start+end) // 2
        stMin[index] = min(initMin(index * 2+1, start, mid), initMin(index * 2+2, mid+1, end))
    return stMin[index]


def Min(index, start, end, left, right):
    if start > right or end < left:
        return float('inf')
    elif left <= start and end <= right:
        return stMin[index]
    else:
        mid = (start + end) // 2
        return min(Min(index*2+1, start, mid, left, right), Min(index*2+2, mid+1, end, left, right))


def Max(index, start, end, left, right):
    if start > right or end < left:
        return 0
    elif left <= start and end <= right:
        return stMax[index]
    else:
        mid = (start + end) // 2
        return max(Max(index * 2 + 1, start, mid, left, right), Max(index * 2 + 2, mid + 1, end, left, right))


N, M = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]
initMin(0, 0, N-1)
initMax(0, 0, N-1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(Min(0, 0, N-1, a-1, b-1), Max(0, 0, N-1, a-1, b-1))
