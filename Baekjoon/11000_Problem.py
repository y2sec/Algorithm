# 11000 강의실 배정

import sys
import heapq

N = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes.sort(key=lambda x: (x[0], x[1]))


end_time = []
room = 0
for cs in classes:
    room = max(room, len(end_time))
    if not end_time:
        heapq.heappush(end_time, cs[1])
        continue
    if end_time[0] > cs[0]:
        heapq.heappush(end_time, cs[1])
    else:
        while end_time:
            if end_time[0] > cs[0]:
                break
            heapq.heappop(end_time)
        heapq.heappush(end_time, cs[1])

print(max(room, len(end_time)))
