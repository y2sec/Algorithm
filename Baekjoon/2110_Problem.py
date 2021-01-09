# 2110 공유기 설치

N, C = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])
result = 0

# 항상 lst[1] - lst[0]이 최소 값이 되는 것은 아님
minV = lst[1] - lst[0]
for i in range(len(lst)-1):
    minV = min(minV, lst[i+1] - lst[i])

maxV = lst[-1] - lst[0]
midV = (minV + maxV) // 2

# 이분 탐색을 통해 값을 구함
while minV <= maxV:
    cnt = 1
    curr = lst[0]
    for i in lst:
        if curr + midV <= i:
            curr = i
            cnt += 1

    if cnt >= C:
        result = max(result, midV)
        minV = midV + 1
    else:
        maxV = midV - 1
    midV = (minV + maxV) // 2

print(result)
