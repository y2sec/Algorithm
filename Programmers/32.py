# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]

    while s != '1':
        length = s.count('1')
        answer[0] += 1
        answer[1] += s.count('0')
        s = str(bin(length))[2:]

    return answer


solution("110010101001")
