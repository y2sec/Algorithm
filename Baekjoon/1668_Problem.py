# 1668 트로피 진열

n = int(input())
# 트로피를 입력받음
trophys = [int(input()) for _ in range(n)]

left_result = 0
right_result = 0

left_max = 0
right_max = 0
# 왼쪽부터 반복문을 돌면서 최대 값을 저장하고 최대값보다 더 크면 +1 해줌
for idx in range(len(trophys)):
    if trophys[idx] > left_max:
        left_result += 1
        left_max = trophys[idx]

for idx in range(len(trophys)-1, -1, -1):
    if trophys[idx] > right_max:
        right_result += 1
        right_max = trophys[idx]

print(left_result)
print(right_result)
