# 2750 수 정렬하기

# 개수를 입력받음
n = int(input())
num_list = list()

# 입력받은 수를 num_list에 저장
for __ in range(n):
    num_list.append(int(input()))

# 정렬
num_list.sort()

# 출력
for num in num_list:
    print(num)
