# 14719 빗물

H, W = map(int, input().split())
block = list(map(int, input().split()))

ans = 0

standard = block[0]
left_cnt = 0
for i in range(1, W):
    if standard <= block[i]:
        standard = block[i]
        ans += left_cnt
        left_cnt = 0
    else:
        left_cnt += (standard - block[i])

standard = block[-1]
right_cnt = 0
for i in range(W-1, -1, -1):
    if standard < block[i]:
        standard = block[i]
        ans += right_cnt
        right_cnt = 0
    else:
        right_cnt += (standard - block[i])

print(ans)
