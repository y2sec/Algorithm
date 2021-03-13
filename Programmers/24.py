#  프린터

def solution(priorities, location):
    answer = 0

    while priorities:
        max_imp = max(priorities)
        imp = priorities.pop(0)
        if imp == max_imp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            if location == 0:
                location += len(priorities)
            else:
                location -= 1
            priorities.append(imp)

    return answer
