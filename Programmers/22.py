# 올바른 괄호

def solution(s):
    isAvailable = 0

    for bracket in s:
        if isAvailable == -1:
            return False

        if bracket == '(':
            isAvailable += 1
        else:
            isAvailable -= 1

    if isAvailable:
        return False

    return True
