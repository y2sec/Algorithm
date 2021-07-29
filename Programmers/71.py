# 이중우선순위큐
import heapq


def solution(operations):
    maxHeap = []
    minHeap = []
    cnt = 0

    for operation in operations:
        if cnt == 0:
            maxHeap = []
            minHeap = []

        op, num = operation.split()

        if op == 'I':
            num = int(num)
            cnt += 1

            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, num)
            continue

        if cnt == 0:
            continue

        cnt -= 1
        if num == '1':
            heapq.heappop(maxHeap)
            continue

        heapq.heappop(minHeap)

    if cnt == 0:
        return [0, 0]

    if cnt == 1:
        return [minHeap[0], minHeap[0]]

    return [-maxHeap[0], minHeap[0]]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))
