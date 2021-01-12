# SRM494 Interesting Party

def solution(first, second):
    field = dict()

    for interested in first:
        if interested in field:
            field[interested] += 1
        else:
            field[interested] = 1

    for interested in second:
        if interested in field:
            field[interested] += 1
        else:
            field[interested] = 1

    return max(field.values())


first = list(input().split())
second = list(input().split())

print(solution(first, second))
