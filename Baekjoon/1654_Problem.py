# 1654 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())
lanline = [int(sys.stdin.readline()) for _ in range(K)]

minLength = 1
maxLength = max(lanline)
midLength = (minLength + maxLength) // 2
res = 0
while minLength <= maxLength:

    cnt = 0
    for lan in lanline:
        cnt += (lan // midLength)

    if cnt >= N:
        res = max(res, midLength)
        minLength = midLength + 1
    else:
        maxLength = midLength - 1
    midLength = (minLength + maxLength) // 2

print(res)
