# 10989 수 정렬하기3

# 입력이 많을때는 sys.stdin.readline()을 사용함으로써 시간을 줄일수 있음
import sys

# 입력에 대한 개수는 많지만 범위를 적으므로 계수 정렬을 이용
n = int(sys.stdin.readline())
num_list = [0 for _ in range(10001)]

# 해당되는 list 번호에 +1 해줌
for __ in range(n):
    num_list[int(sys.stdin.readline())] += 1

# 해당 list 번호에 수만큼 출력
for num in range(10001):
    for __ in range(num_list[num]):
        print(num)
