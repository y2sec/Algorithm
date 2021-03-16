# 숫자의표현

def solution(n):
    answer = 1
    number = [x for x in range(10001)]

    s_idx = 1
    e_idx = 2

    while s_idx < n:
        c_n = sum(number[s_idx:e_idx])
        if c_n == n:
            answer += 1
            s_idx += 1
        elif c_n > n:
            s_idx += 1
        else:
            e_idx += 1
    return answer
