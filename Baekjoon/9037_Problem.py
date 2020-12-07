# 9037 The candy war

T = int(input())

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    result = 0
    # 홀수개의 사탕을 가진 아이를 짝수개로 만들어줌
    for i in range(N):
        if C[i] % 2 == 1:
            C[i] += 1

    while True:
        # 사탕의 수를 set에 넣어줌으로써 모두 같은지 확인
        isSame = set()
        isSame.update(C)
        if len(isSame) == 1:
            break
        # 동시에 나눠주기 위해 미리 저장해둠
        giveout = list()
        for i in range(N):
            C[i] = C[i] // 2
            giveout.append(C[i])
        # 사탕 순환
        for i in range(N):
            if i == N-1:
                C[0] += giveout[i]
            else:
                C[i+1] += giveout[i]
        # 홀수개의 사탕을 가진 아이를 짝수개로 만들어줌
        for i in range(N):
            if C[i] % 2 == 1:
                C[i] += 1
        result += 1

    print(result)
