# n진수 게임

def solution(n, t, m, p):
    answer = ''

    def conversion(num, n):
        result = ''

        numbers = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                   12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        while num >= n:
            r = num % n
            result = numbers[r] + result
            num //= n

        result = numbers[num] + result

        return result

    data = ''
    cnt = 0
    while len(data) < t * m:
        data += conversion(cnt, n)
        cnt += 1

    if m == p:
        p = 0

    for idx in range(1, len(data)+1):
        if len(answer) >= t:
            break

        if idx % m == p:
            answer += data[idx-1]

    return answer


print(solution(16, 16, 2, 2))
