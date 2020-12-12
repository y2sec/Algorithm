# 11399 ATM

N = int(input())
P = sorted(list(map(int, input().split())))
result = 0

# 해당 사람이 걸린 시간은 앞 사람 걸린 시간에 자기의 시간을 더한 값
for i in range(1, N+1):
    result += sum(P[:i])

print(result)
