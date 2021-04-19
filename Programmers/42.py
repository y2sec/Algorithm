# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    words = s.split()

    isBlank = True
    for w in s:
        if w.isspace():
            answer += w
            isBlank = True
            continue

        if isBlank:
            answer += w.upper()
            isBlank = False
        else:
            answer += w.lower()

    return answer
