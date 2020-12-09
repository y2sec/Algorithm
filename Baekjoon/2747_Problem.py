# 2747 피보나치 수

def fibonacci(n):
    global result
    # n이 2보다 작으면 자신을 리턴(피보나치의 0과 1값은 각각 0과 1임
    if n < 2:
        return n
    # 리스트에 이미 값이 존재하면 해당 값을 리턴
    elif result[n] is not None:
        return result[n]
    # 값이 존재하지 않으면 값을 구해줌
    else:
        result[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return result[n]


N = int(input())
# 최대 입력 값이 45이므로 리스트의 크기를 정함
result = [None for _ in range(46)]
print(fibonacci(N))
