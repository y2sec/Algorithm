# 만들 수 없는 금액

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

cnt = 0
for coin in coins:
    if cnt+1 >= coin:
        cnt += coin
    else:
        print(cnt+1)
        break
