# SRM443D2 CirclesCountry
from math import sqrt


# 두 점이 경계를 지나는 경우는 시작점이 원 안에 있는데 끝점은 없는 경우 혹은 그 반대 경우만 존재함
def inCircle(x, y, r):
    start = False
    end = False

    if sqrt(pow(x - x1, 2) + pow(y - y1, 2)) <= r:
        start = True
    if sqrt(pow(x - x2, 2) + pow(y - y2, 2)) <= r:
        end = True

    return start != end


# X = [0, -6, 6]
# Y = [0, 1, 2]
# R = [2, 2, 2]
# x1 = -5
# y1 = 1
# x2 = 5
# y2 = 1

X = [1, -3, 2, 5, -4, 12, 12]
Y = [1, -1, 2, 5, 5, 1, 1]
R = [8, 1, 2, 1, 1, 1, 2]
x1 = -5
y1 = 1
x2 = 12
y2 = 1

ans = 0

for i in range(len(X)):
    if inCircle(X[i], Y[i], R[i]):
        ans += 1

print(ans)
