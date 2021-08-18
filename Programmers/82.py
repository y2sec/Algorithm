# 야근 지수

def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0

    works.sort(reverse=True)

    save = 1
    for i in range(1, len(works)):
        diff = works[i-1] - works[i]
        if diff * i > n:
            break

        save += 1
        n -= (diff * i)
        for j in range(i):
            works[j] -= diff

    i = 0
    while n > 0:
        works[i % save] -= 1
        i += 1
        n -= 1

    for work in works:
        answer += (work ** 2)

    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
