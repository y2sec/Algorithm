# 짝지어 제거하기

def solution(s):
    stack = []

    for w in s:
        if not stack:
            stack.append(w)
            continue

        if stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    return 0 if stack else 1
