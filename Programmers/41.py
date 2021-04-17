# 괄호 회전하기

def solution(s):
    answer = len(s)

    brackets = {']': '[', '}': '{', ')': '('}

    for index in range(len(s)):
        bracketStack = []
        isValid = True
        for bracket in s[index:] + s[:index]:
            if bracket in ['[', '{', '(']:
                bracketStack.append(bracket)
                continue

            if not bracketStack or brackets[bracket] != bracketStack.pop():
                isValid = False
                break

        if not isValid or bracketStack:
            answer -= 1

    return answer
