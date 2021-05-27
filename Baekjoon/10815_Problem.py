# 10815 숫자 카드

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
numbers = list(map(int, input().split()))

result = [0 for _ in range(M)]

for index, number in enumerate(numbers):
    minIndex = 0
    maxIndex = N-1
    midIndex = (minIndex + maxIndex) // 2

    while minIndex <= maxIndex:
        if cards[midIndex] == number:
            result[index] = 1
            break

        if cards[midIndex] < number:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1

        midIndex = (minIndex + maxIndex) // 2

for find in result:
    print(find, end=' ')
