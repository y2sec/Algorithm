# 문자열 재정렬

S = list(input())
sort = []
num = 0

for s in S:
    if ord('A') <= ord(s) <= ord('Z'):
        sort.append(s)
    else:
        num += int(s)

sort.sort()

for s in sort:
    print(s, end='')

if num:
    print(num)
