# 16769 Mixing Milk

milks = list()

for _ in range(3):
    milks.append(list(map(int, input().split())))

curr_bottle = 0
for _ in range(100):
    if curr_bottle == 2:
        milks[0][1] += milks[curr_bottle][1]
        milks[curr_bottle][1] = 0
        if milks[0][0] < milks[0][1]:
            diff = milks[0][1] - milks[0][0]
            milks[curr_bottle][1] += diff
            milks[0][1] -= diff
        curr_bottle = 0
    else:
        milks[curr_bottle+1][1] += milks[curr_bottle][1]
        milks[curr_bottle][1] = 0
        if milks[curr_bottle+1][0] < milks[curr_bottle+1][1]:
            diff = milks[curr_bottle+1][1] - milks[curr_bottle+1][0]
            milks[curr_bottle][1] += diff
            milks[curr_bottle+1][1] -= diff
        curr_bottle += 1

for milk in milks:
    print(milk[1])
