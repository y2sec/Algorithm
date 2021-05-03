# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [['*', 7, 4, 1],
              [0, 8, 5, 2],
              ['#', 9, 6, 3]]

    leftHand, rightHand = '*', '#'

    def getFromHandToKey(hand, key):
        handPosition = getPosition(hand)
        keyPosition = getPosition(key)

        return abs(handPosition[0] - keyPosition[0]) + abs(handPosition[1] - keyPosition[1])

    def getPosition(key):
        for x in range(3):
            for y in range(4):
                if keypad[x][y] == key:
                    return x, y

    for number in numbers:
        if number in keypad[0]:
            answer += 'L'
            leftHand = number
            continue

        if number in keypad[2]:
            answer += 'R'
            rightHand = number
            continue

        leftHandLength = getFromHandToKey(leftHand, number)
        rightHandLength = getFromHandToKey(rightHand, number)

        if leftHandLength > rightHandLength:
            answer += 'R'
            rightHand = number
            continue

        if leftHandLength < rightHandLength:
            answer += 'L'
            leftHand = number
            continue

        if hand == 'right':
            answer += 'R'
            rightHand = number
        else:
            answer += 'L'
            leftHand = number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
