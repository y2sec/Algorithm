# 1920 수 찾기

n = int(input())
n_list = dict()
input_list = list(map(int, input().split(' ')))

# 시간 초과를 고려하여 dict에 수를 저장
for num in input_list:
    n_list[num] = 1

m = int(input())
m_list = list(map(int, input().split(' ')))

# 숫자가 존재하는지 확인
for num in m_list:
    if num in n_list:
        print(1)
    else:
        print(0)
