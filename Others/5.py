# 모험가 길드

N = int(input())
lst = sorted(list(map(int, input().split())))

ans = 0
idx = 0
while idx < N:
    if idx + lst[idx] >= N:
        idx += 1
    else:
        ans += 1
        idx += lst[idx]

print(ans)
