# 2470 두 용액

N = int(input())
lq = sorted(list(map(int, input().split())))

result = [lq[0], lq[-1]]
acidity = lq[0] + lq[-1]

leftP, rightP = 0, len(lq) - 1

while leftP < rightP:
    currAcidity = lq[leftP] + lq[rightP]

    if abs(0 - currAcidity) < abs(0 - acidity):
        result[0], result[1] = lq[leftP], lq[rightP]
        acidity = currAcidity

    if currAcidity >= 0:
        rightP -= 1
    else:
        leftP += 1

    if acidity == 0:
        break

print(result[0], result[1])
