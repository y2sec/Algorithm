# 20950 미술가 미미

import itertools


def diff(rgb1, rgb2):
    return abs(rgb1[0] - rgb2[0]) + abs(rgb1[1] - rgb2[1]) + abs(rgb1[2] - rgb2[2])


def combination(rgbs):
    cRGB = [0, 0, 0]
    for rgb in rgbs:
        cRGB[0] += rgb[0]
        cRGB[1] += rgb[1]
        cRGB[2] += rgb[2]

    return [cRGB[0] // len(rgbs), cRGB[1] // len(rgbs), cRGB[2] // len(rgbs)]


N = int(input())
RGBs = [list(map(int, input().split())) for _ in range(N)]
gRGB = list(map(int, input().split()))

ans = float('inf')
for i in range(2, 8):
    for rgbs in list(itertools.combinations(RGBs, i)):
        mRGB = combination(rgbs)
        res = diff(gRGB, mRGB)
        if ans > res:
            ans = res
print(ans)
