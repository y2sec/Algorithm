# 추석 트래픽
import datetime


def solution(lines):
    answer = 0

    traffics = []
    for line in lines:
        day, time, need = line.split()
        endTime = datetime.datetime.strptime(day + time, '%Y-%m-%d%H:%M:%S.%f')
        traffics.append((endTime - datetime.timedelta(seconds=float(need[:-1]) - 0.001), endTime))

    traffics.sort(key=lambda x: x[1])

    for k in range(2):
        for i in range(len(traffics)):
            startTime = traffics[i][k]
            endTime = startTime + datetime.timedelta(seconds=0.999)
            cnt = 1
            for j in range(i + 1, len(traffics)):
                if traffics[j][0] <= startTime <= traffics[j][1]:
                    cnt += 1
                    continue

                if traffics[j][0] <= endTime <= traffics[j][1]:
                    cnt += 1
                    continue

                if startTime <= traffics[j][0] <= endTime:
                    cnt += 1
                    continue

            answer = max(answer, cnt)

    return answer


# print(solution([
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ]))

# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
