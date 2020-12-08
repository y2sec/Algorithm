# 11650 좌표 정렬하기


n = int(input())
location_list = list()

# 튜플 형태로 입력받아 list에 넣음
for _ in range(n):
    location = tuple(map(int, input().split()))
    location_list.append(location)

# 정렬 우선순위를 x좌표 -> y좌표 순으로 함
location_list = sorted(location_list, key=lambda x: (x[0], x[1]))

for location in location_list:
    print(location[0], location[1])
