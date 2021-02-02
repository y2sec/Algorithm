# 1931 회의실 배정

N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
T = max([max(x) for x in conference])
table = [True for _ in range(T + 1)]

for i in range(N):
    conference[i].append(conference[i][1] - conference[i][0])

conference.sort(key=lambda x: (x[1], x[0], x[2]))

ans = 0
endtime = 0
for cf in conference:
    if endtime <= cf[0]:
        ans += 1
        endtime = cf[1]
print(ans)
