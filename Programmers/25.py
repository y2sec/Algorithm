# 신규 아이디 추천

def solution(new_id):
    answer = []
    new_id = new_id.lower()

    for s in new_id:
        if 'a' <= s <= 'z' or '0' <= s <= '9' or s == '-' or s == '_' or s == '.':
            answer.append(s)
    idx = 0
    while idx < len(answer) - 1:
        if answer[idx] == '.' and answer[idx + 1] == '.':
            answer.pop(idx)
            continue
        idx += 1

    while len(answer) > 0 and (answer[0] == '.' or answer[-1] == '.'):
        if answer[0] == '.':
            answer.pop(0)

        elif answer[-1] == '.':
            answer.pop()

    if len(answer) == 0:
        answer.append('a')

    if len(answer) >= 16:
        answer = answer[:15]
        while len(answer) > 0 and (answer[0] == '.' or answer[-1] == '.'):
            if answer[0] == '.':
                answer.pop(0)
            elif answer[-1] == '.':
                answer.pop()
    elif len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[-1])

    return ''.join(answer)
