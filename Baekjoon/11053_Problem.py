# 11053 가장 긴 증가하는 부분 수열

n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)
sequence = [0] * (n + 1)

for i in range(1, n + 1):
    length = 0
    for j in range(0, i):
        if data[i] > data[j]:
            length = max(length, sequence[j])
    sequence[i] = length + 1

print(max(sequence))