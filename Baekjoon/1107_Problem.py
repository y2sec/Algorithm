# 1107 리모컨

N = int(input())
M = int(input())
button = []

if M > 0:
    button = list(input().split())

answer = max(N - 100, 100 - N)

for channel in range(N, 1000001):
    isAvailable = True
    for number in str(channel):
        if number in button:
            isAvailable = False
            break

    if isAvailable:
        answer = min(answer, len(str(channel)) + channel - N)
        break

for channel in range(N, -1, -1):
    isAvailable = True
    for number in str(channel):
        if number in button:
            isAvailable = False
            break

    if isAvailable:
        answer = min(answer, len(str(channel)) + N - channel)
        break

print(answer)
