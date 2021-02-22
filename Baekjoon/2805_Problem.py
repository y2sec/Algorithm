# 2805 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))

minV = 0
maxV = max(trees)
midV = (minV + maxV) // 2

res = 0
while minV <= maxV:
    cnt = 0
    for tree in trees:
        if tree >= midV:
            cnt += tree - midV

    if cnt >= M:
        res = max(res, midV)
        minV = midV + 1
    else:
        maxV = midV - 1

    midV = (minV + maxV) // 2

print(res)
