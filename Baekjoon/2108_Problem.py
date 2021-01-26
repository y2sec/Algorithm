# 2108 통계학

N = int(input())
data = []
freq = dict()
for _ in range(N):
    ip = int(input())
    data.append(ip)
    if ip in freq:
        freq[ip] += 1
    else:
        freq[ip] = 1

data.sort()
freq = sorted(freq.items(), key=lambda x: (x[1], -x[0]), reverse=True)

print(round(sum(data)/N))
print(data[N//2])
if len(data) == 1:
    print(data[0])
elif freq[0][1] == freq[1][1]:
    print(freq[1][0])
else:
    print(freq[0][0])
print(max(data) - min(data))
