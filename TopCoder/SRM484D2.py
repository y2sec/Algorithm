# SRM484D2 NumberMagicEasy

answer = 'NYNY'
cardLst = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 9, 10, 11, 12], [1, 2, 5, 6, 9, 10, 13, 14], [1, 3, 5, 7, 9, 11, 13, 15]]
card = [0 for _ in range(16)]

for i in range(len(answer)):
    if answer[i] == 'Y':
        for n in cardLst[i]:
            card[n-1] += 1
    else:
        for n in cardLst[i]:
            card[n-1] -= 1

print(card.index(max(card))+1)
