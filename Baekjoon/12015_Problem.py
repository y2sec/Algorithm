# 12015 가장 긴 증가하는 부분 수열 2

N = int(input())
lst = list(map(int, input().split()))
res = [lst[0]]

for i in range(1, N):
    if lst[i] > res[-1]:
        res.append(lst[i])

    else:
        start = 0
        end = len(res)
        mid = (start + end) // 2
        cnt = float('inf')
        while start <= end:
            if res[mid] >= lst[i]:
                cnt = min(cnt, mid)
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        res[cnt] = lst[i]

print(len(res))
