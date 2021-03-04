# 무지의 먹방 라이브

def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    food_times_sort = sorted(food_times)
    foods = len(food_times)
    cnt = 0
    if k // foods >= food_times_sort[0]:
        cnt = food_times_sort[0]
        k -= food_times_sort[0] * foods
        foods -= 1
    else:
        return k % foods + 1

    for i in range(1, len(food_times)):
        div = food_times_sort[i] - food_times_sort[i - 1]
        if k // foods >= div:
            cnt = food_times_sort[i]
            k -= div * foods
            foods -= 1
        else:
            k = k % foods
            for j in range(len(food_times)):
                if food_times[j] <= cnt:
                    continue
                if k == 0:
                    return j + 1
                if food_times[j] > cnt:
                    k -= 1

    return answer


print(solution([1, 1, 1, 1, 1, 1], 1))
