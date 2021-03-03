# 곱하기 혹은 더하기

lst = list(map(int, input()))

res = lst[0]
for i in range(1, len(lst)):
    plus = res + lst[i]
    multi = res * lst[i]
    res = max(plus, multi)

print(res)
