# 1427 소트인사이드

# 숫자를 입력받음
num = input()

# 9부터 확인하면서 숫자가 입력받은 숫자에 있으면 출력
for i in range(9, -1, -1):
    for j in num:
        if int(j) == i:
            print(i, end='')
