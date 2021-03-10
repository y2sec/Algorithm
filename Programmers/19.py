# 튜플

def solution(s):
    answer = []
    change = []
    for tp in s.split('},{'):
        tp = tp.replace('{', '').replace('}', '')
        lst = []
        for t in tp.split(','):
            lst.append(int(t))
        change.append(lst)

    change.sort(key=lambda x: len(x))

    for lst in change:
        for n in lst:
            if n not in answer:
                answer.append(n)

    return answer
