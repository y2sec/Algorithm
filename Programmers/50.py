# 압축

def solution(msg):
    answer = []
    dictionary = dict()
    for i in range(26):
        dictionary[chr(65 + i)] = i + 1

    index = 27
    currIdx = 0
    while currIdx < len(msg):
        longStrIdx = currIdx + 1
        for i in range(currIdx + 1, len(msg) + 2):
            if msg[currIdx:i] in dictionary:
                longStrIdx = i
            else:
                break

        answer.append(dictionary[msg[currIdx:longStrIdx]])
        dictionary[msg[currIdx:longStrIdx + 1]] = index
        index += 1
        currIdx = longStrIdx
    return answer
