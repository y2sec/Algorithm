# 불량 사용자

import itertools


def solution(user_id, banned_id):
    banned = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        for uid in user_id:
            if len(banned_id[i]) != len(uid):
                continue

            isValid = True
            for sidx in range(len(uid)):
                if banned_id[i][sidx] != '*' and banned_id[i][sidx] != uid[sidx]:
                    isValid = False
                    break

            if isValid:
                banned[i].append(uid)
    data = []
    for comb in itertools.product(*banned):
        if len(set(comb)) != len(comb):
            continue
        data.append(tuple(sorted(list(comb))))

    return len(set(data))


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])