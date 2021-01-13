# SRM428 ThePalindrome

def solution(s):
    start, end = 0, len(s)-1
    lst = list(s)

    while start <= end:
        print(start, end)
        if lst[start] != lst[end]:
            lst.insert(end+1, lst[start])
        else:
            end -= 1
        start += 1

    print(len(lst))


solution(input())
