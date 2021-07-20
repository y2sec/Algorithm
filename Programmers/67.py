# 단어 변환
import collections


def isChange(wordA, wordB):
    cnt = 0
    for idx in range(len(wordA)):
        if wordA[idx] == wordB[idx]:
            cnt += 1

    return True if cnt + 1 == len(wordA) else False


def solution(begin, target, words):
    wordsCnt = collections.defaultdict()
    for word in words:
        wordsCnt[word] = float('inf')

    queue = collections.deque()
    queue.append((begin, 0))

    while queue:
        current, cnt = queue.popleft()

        for word in words:
            if not isChange(current, word):
                continue

            if wordsCnt[word] <= cnt + 1:
                continue

            wordsCnt[word] = cnt + 1
            queue.append((word, wordsCnt[word]))

    return 0 if target not in wordsCnt or wordsCnt[target] == float('inf') else wordsCnt[target]


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
