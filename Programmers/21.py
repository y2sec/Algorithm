# 다음 큰 숫자

def solution(n):
    answer = 0

    binaryN = bin(n)
    n_one = str(binaryN).count('1')

    def isAvailable(N):
        binaryNxtN = bin(N)
        nxtN_one = str(binaryNxtN).count('1')

        if n_one == nxtN_one:
            return True
        return False

    nxtN = n + 1
    while True:
        if isAvailable(nxtN):
            answer = nxtN
            break
        nxtN += 1

    return answer
