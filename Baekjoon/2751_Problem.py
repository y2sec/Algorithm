# 2751 수 정렬하기2

import sys

# n의 개수가 최대 1000000이기때문에 input()이 아닌 sys.stdin.readline()으로 입력을 처리
n = int(sys.stdin.readline())
result = list()
for _ in range(n):
    result.append(int(sys.stdin.readline()))

# 정렬 후 출력
result.sort()
for num in result:
    print(num)
