# SRM480D2 Cryptography

def solution(numbers):
    result = 0

    for i in range(len(numbers)):
        numbers[i] += 1
        cnt = 1
        for number in numbers:
            cnt *= number
        numbers[i] -= 1

        result = max(result, cnt)

    return result


numbers = list(map(int, input().split()))
print(solution(numbers))
