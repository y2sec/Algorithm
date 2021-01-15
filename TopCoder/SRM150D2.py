# SRM150D2 InterestingDigits

def conversion(number, base):
    strNum = []
    while number > 0:
        strNum.insert(0, str(number % base))
        number //= base

    ans = 0
    for n in strNum:
        ans += int(n)

    return ans


def solution(base):
    ans = []
    for i in range(2, base):
        isAvailable = True
        for j in range(i, 1000, i):
            if conversion(j, base) % i != 0:
                isAvailable = False
                break

        if isAvailable:
            ans.append(i)

    return ans


print(solution(int(input())))
