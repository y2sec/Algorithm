# 2484 주사위 네개

N = int(input())

# 각 사람의 상금을 0으로 초기화
result = [0 for _ in range(N)]

# 상금을 구해줌
for i in range(N):
    dice = sorted(list(map(int, input().split())))
    dice_set = set(dice)
    if len(dice_set) == 1:
        result[i] = 50000 + dice[0] * 5000
    elif len(dice_set) == 2:
        # 같은 수가 3개인 경우
        if dice[1] == dice[2]:
            result[i] = 10000 + dice[1] * 1000
        # 같은 수가 2개인 경우가 두 쌍인 경우
        else:
            result[i] = 2000 + dice[1] * 500 + dice[2] * 500
    elif len(dice_set) == 3:
        for j in range(3):
            if dice[j] == dice[j+1]:
                result[i] = 1000 + dice[j] * 100
                break
    else:
        result[i] = dice[3] * 100

print(max(result))
