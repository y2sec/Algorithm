# 풍선 터트리기

def solution(a):
    answer = 2

    left = [0 for _ in range(len(a))]
    right = [0 for _ in range(len(a))]

    left[0] = a[0]
    right[-1] = a[-1]

    for i in range(1, len(a)):
        left[i] = a[i] if left[i-1] > a[i] else left[i-1]

    for i in range(len(a)-2, -1, -1):
        right[i] = a[i] if right[i+1] > a[i] else right[i+1]

    for i in range(1, len(a)-1):
        if left[i-1] < a[i] and a[i] > right[i+1]:
            continue

        answer += 1

    return answer


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
