# 타겟 넘버

import collections


def solution(numbers, target):
    def bfs():
        cnt = 0
        length = len(numbers)

        queue = collections.deque()
        queue.append((numbers[0], 1))
        queue.append((-numbers[0], 1))

        while queue:
            number, i = queue.popleft()

            if i == length:
                if number == target:
                    cnt += 1
                continue

            queue.append((number + numbers[i], i + 1))
            queue.append((number - numbers[i], i + 1))
        return cnt

    return bfs()

