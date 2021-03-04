# 오픈 채팅방

def solution(record):
    answer = []
    nickname = dict()

    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(r[1] + '님이 들어왔습니다.')
            nickname[r[1]] = r[2]
        elif r[0] == 'Leave':
            answer.append(r[1] + '님이 나갔습니다.')
        else:
            nickname[r[1]] = r[2]

    for i in range(len(answer)):
        answer[i] = nickname[answer[i][:answer[i].index('님')]] + answer[i][answer[i].index('님'):]

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
