# SRM363D2 HandShaking
# 카탈랑 수
n = 10

handshaking = [0 for _ in range(n//2+1)]
handshaking[0] = 1

for i in range(1, n//2+1):
    for j in range(i):
        handshaking[i] += handshaking[j] * handshaking[i-j-1]

print(handshaking[n//2])
