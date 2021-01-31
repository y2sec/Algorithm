# 4949 균형잡힌 세상

string = input()

while string != '.':
    stack = []
    bracket = True
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' or s == ']':
            if len(stack) == 0:
                bracket = False
                break
            b = stack.pop()
            if b == '(' and s == ')' or b == '[' and s == ']':
                continue
            else:
                bracket = False
                break

    if len(stack) > 0:
        bracket = False

    print('yes' if bracket else 'no')

    string = input()
