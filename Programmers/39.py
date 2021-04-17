# 영어 끝말잇기

def solution(n, words):
    useWords = [words[0]]
    lastChar = words[0][-1]

    order = -1
    for index in range(1, len(words)):
        if lastChar != words[index][0]:
            order = index
            break

        if words[index] in useWords:
            order = index
            break

        useWords.append(words[index])
        lastChar = words[index][-1]

    if order == -1:
        return [0, 0]

    return [order % n + 1, order // n + 1]
