# 10816 숫자 카드 2

N = int(input())
lst = list(map(int, input().split()))
have_card = dict()

for num in lst:
    if num not in have_card:
        have_card[num] = 1
    else:
        have_card[num] += 1

M = int(input())
need_have_lst = list(map(int, input().split()))

lst = sorted(have_card.keys())

for num in need_have_lst:
    min_term = 0
    max_term = len(lst) - 1
    mid = (min_term + max_term) // 2

    find = False
    while min_term <= max_term:
        if num == lst[mid]:
            print(have_card[num], end=' ')
            find = True
            break
        elif num > lst[mid]:
            min_term = mid + 1
        else:
            max_term = mid - 1
        mid = (min_term + max_term) // 2

    if not find:
        print(0, end=' ')
