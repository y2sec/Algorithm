# 16676 근우의 다이어리 꾸미기

N = int(input())
result = 1
num = 1
"""
N < 11 -> 1개
N < 111 -> 2개
N < 1111 -> 3개
이러한 규칙을 가지고 있음
"""
for i in range(10):
    if num > N:
        break
    result = i+1
    num = num * 10 + 1
print(result)
