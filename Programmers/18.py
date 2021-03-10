# 쿼드압축 후 개수 세기

def solution(arr):
    answer = [0, 0]

    def dac(N, sx, sy, arr):
        if N == 1:
            answer[arr[sx][sy]] += 1
            return

        standard = arr[sx][sy]
        isSame = True
        for i in range(sx, sx + N):
            for j in range(sy, sy + N):
                if arr[i][j] != standard:
                    isSame = False
                    break
            if not isSame:
                break

        if isSame:
            answer[standard] += 1
            return
        dac(N // 2, sx, sy, arr)
        dac(N // 2, sx + N // 2, sy, arr)
        dac(N // 2, sx, sy + N // 2, arr)
        dac(N // 2, sx + N // 2, sy + N // 2, arr)

    dac(len(arr), 0, 0, arr)
    return answer
