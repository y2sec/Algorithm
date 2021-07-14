# 디스크 컨트롤러
import heapq


def solution(jobs):
    answer = 0

    countJob = len(jobs)

    heapq.heapify(jobs)
    jobHeap = []

    req, time = heapq.heappop(jobs)
    ms = req
    heapq.heappush(jobHeap, [time, req])

    while jobHeap:
        time, req = heapq.heappop(jobHeap)
        answer += (ms + time) - req
        ms += time

        if jobs and not jobHeap:
            ms = max(ms, jobs[0][0])

        while jobs and ms >= jobs[0][0]:
            req, time = heapq.heappop(jobs)
            heapq.heappush(jobHeap, [time, req])

    return answer // countJob


print(solution([[0, 3], [1, 9], [2, 6]]))
