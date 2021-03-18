# 10162 전자레인지

T = int(input())
res = [0, 0, 0]
time = [300, 60, 10]

for time_idx in range(len(time)):
    if T >= time[time_idx]:
        res[time_idx] += (T // time[time_idx])
        T %= time[time_idx]

if not T:
    print(res[0], res[1], res[2])
else:
    print(-1)
