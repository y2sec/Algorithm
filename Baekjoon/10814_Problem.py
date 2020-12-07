# 10814 나이순 정렬

# 사람 수를 입력받음
n = int(input())
member_list = list()

# 정보를 입력받고 튜플로 list에 삽입
for i in range(n):
    member = input().split(' ')
    member_list.append((int(member[0]), member[1]))

# 나이를 기준으로 정렬
member_list = sorted(member_list, key=lambda x: x[0])

for age, name in member_list:
    print(age, name)
