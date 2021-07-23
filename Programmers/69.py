# 셔틀버스
import datetime
import collections

YEAR = 2021
MONTH = 7
DAY = 23
SECOND = 0


def solution(n, t, m, timetable):
    answer = ''

    timetable.sort()

    dateTimeTable = collections.deque()
    for time in timetable:
        hour, minute = time.split(':')
        dateTimeTable.append(datetime.datetime(YEAR, MONTH, DAY, int(hour), int(minute), SECOND))

    startHour = 9
    startMinute = 0
    currentTime = datetime.datetime(YEAR, MONTH, DAY, startHour, startMinute, SECOND)

    wait = collections.deque()
    for bus in range(n):

        while dateTimeTable and dateTimeTable[0] <= currentTime:
            wait.append(dateTimeTable.popleft())

        if len(wait) >= m:
            answer = wait[m - 1] - datetime.timedelta(minutes=1)
        else:
            answer = currentTime

        for cnt in range(m):
            if not wait:
                break
            wait.popleft()

        currentTime += datetime.timedelta(minutes=t)

    return answer.strftime("%H:%M")


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
