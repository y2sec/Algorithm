# 2480 주사위 세개

dice = list(map(int, input().split()))

# set에 넣어 길이에 따라 중복된 수가 얼마나 있는지 확인
if len(set(dice)) == 3:
    print(max(dice) * 100)
elif len(set(dice)) == 2:
    print(1000 + sorted(dice)[1] * 100)
else:
    print(10000 + dice[0] * 1000)
