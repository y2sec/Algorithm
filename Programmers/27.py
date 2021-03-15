# 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    p, y = s.count('p'), s.count('y')

    return p == y
