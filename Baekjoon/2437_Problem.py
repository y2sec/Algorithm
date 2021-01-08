# 2437 저울

N = int(input())
lst = sorted(list(map(int, input().split())))

result = 0

"""
ex) 5까지 만들어진다면 다음 수가 그보다 1 더 큰 6보다 작거나 같기만 해도 두 수를 더한 값만큼은 더 만들 수 있음
"""
for n in lst:
    if n <= result+1:
        result += n
    else:
        break
print(result+1)
