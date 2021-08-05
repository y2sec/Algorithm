# 부족한 금액 계산하기

def solution(price, money, count):
    return max(0, ((count*(count+1)//2) * price) - money)


print(solution(3, 20, 4))
