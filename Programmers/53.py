# 보석 쇼핑

def solution(gems):
    totalGems = set(gems)
    answer = [0, 0]
    gemLeng = len(gems)

    Leng = float('inf')
    l, r = 0, 0
    gem = dict()

    find = False
    while l < gemLeng and r < gemLeng:
        if not find:
            if gems[r] not in gem:
                gem[gems[r]] = 1
            else:
                gem[gems[r]] += 1

        if len(gem) == len(totalGems):
            if Leng > abs(r - l):
                Leng = abs(r - l)
                answer[0] = l + 1
                answer[1] = r + 1

            gem[gems[l]] -= 1
            if gem[gems[l]] == 0:
                del gem[gems[l]]
            l += 1
            find = True
            continue
        r += 1
        find = False

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "A", "B"]))
