# 후보키

import itertools


def solution(relation):
    col = len(relation[0])
    row = len(relation)
    keys = []
    tuples = [x for x in range(col)]

    for i in range(1, len(tuples)+1):
        for com in list(itertools.combinations(tuples, i)):
            isAvail = True
            for key in keys:
                if set(key).issubset(com):
                    isAvail = False

            if not isAvail:
                continue

            key_set = set()
            for j in range(row):
                lst = tuple([relation[j][k] for k in com])
                key_set.add(lst)
            if len(key_set) == row:
                keys.append(com)
    print(keys)
    return len(keys)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
