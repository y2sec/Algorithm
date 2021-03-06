# 1449 수리공 항승

N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
cnt = 1
start = lst[0]
for i in range(1, N):
    if lst[i] - start <= L - 1:
        continue
    else:
        start = lst[i]
        cnt += 1

print(cnt)
