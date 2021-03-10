# 큰 수 만들기

def solution(number, k):
    answer = ''

    s = 0
    e = k + 1
    length = len(number)
    for i in range(length - k):
        max_n = '0'
        for j in range(s, e):
            if number[j] > max_n:
                s = j + 1
                max_n = number[j]
            if max_n == '9':
                break
        e += 1
        answer += max_n

    return answer
