# 광고 삽입

def solution(play_time, adv_time, logs):
    answer = ''

    play_time_ts = int(play_time[:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:8])
    adv_time_ts = int(adv_time[:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:8])

    adv = [0] * 360000
    logs_start_sec = []
    logs_end_sec = []
    for log in logs:
        start_ts = int(log[:2]) * 3600 + int(log[3:5]) * 60 + int(log[6:8])
        end_ts = int(log[9:11]) * 3600 + int(log[12:14]) * 60 + int(log[15:17])
        logs_start_sec.append(start_ts)
        logs_end_sec.append(end_ts)

    total_time = [0] * 360000
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1

    for i in range(1, play_time_ts):
        total_time[i] += total_time[i-1]
    for i in range(1, play_time_ts):
        total_time[i] += total_time[i-1]

    max_time = 0
    adv_start_time = 0

    for i in range(adv_time_ts-1, play_time_ts):
        if i >= adv_start_time:
            if max_time < total_time[i] - total_time[i - adv_time_ts]:
                max_time = total_time[i] - total_time[i - adv_time_ts]
                adv_start_time = i + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                adv_start_time = i + 1

    adv_start_time -= adv_time_ts

    h = adv_start_time // 3600
    adv_start_time %= 3600
    m = adv_start_time // 60
    adv_start_time %= 60
    s = adv_start_time
    answer += '%02d:%02d:%02d' % (h, m, s)
    print(answer)
    return answer


solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
