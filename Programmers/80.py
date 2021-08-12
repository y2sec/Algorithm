# 110 옮기기

def solution(s):
    answer = [None for _ in range(len(s))]

    for idx in range(len(s)):
        answer[idx] = find(s[idx])

    return answer


def find(s):
    count = 0

    leftStack = list(s)
    rightStack = list()

    while leftStack:
        value = leftStack.pop()

        if value == '0' and leftStack[-2:] == ['1', '1']:
            leftStack.pop()
            leftStack.pop()
            count += 1
            cnt = 0
            while rightStack and cnt < 2:
                leftStack.append(rightStack.pop())
                cnt += 1
        else:
            rightStack.append(value)

    s = ''.join(rightStack[-1::-1])

    m = '110' * count
    if s == '1':
        s = m + s
    elif s.find('11') != -1:
        i = s.find('11')
        s = s[:i] + m + s[i:]
    else:
        i = s.rfind('0')
        s = s[:i+1] + m + s[i+1:]

    return s


# print(solution(["1110", "100111100", "0111111010"]))
# print(solution(["1011110", "01110", "101101111010"]))
print(solution(["1100111011101001", "110"]))
