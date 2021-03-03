# 1744 수 묶기

import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
number = [[], []]

for num in lst:
    if num > 0:
        number[0].append(num)
    else:
        number[1].append(num)

number[0].sort(reverse=True)
number[1].sort()

res = 0
for i in range(2):
    idx = 0
    while idx < len(number[i]):
        if idx+1 >= len(number[i]):
            res += number[i][idx]
            idx += 1
        else:
            plus = number[i][idx] + number[i][idx+1]
            multi = number[i][idx] * number[i][idx+1]
            if plus > multi:
                res += number[i][idx]
                idx += 1
            else:
                res += multi
                idx += 2

print(res)
