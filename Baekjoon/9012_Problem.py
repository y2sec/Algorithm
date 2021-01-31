# 9012 괄호

T = int(input())

for _ in range(T):
    stack = []
    VPS = True
    for bracket in input():
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                VPS = False
                break
            stack.pop()
    if len(stack) > 0:
        VPS = False
    print('YES' if VPS else 'NO')
