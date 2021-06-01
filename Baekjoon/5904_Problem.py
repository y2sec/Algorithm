# 5904 Moo 게임

def find(m, moo, N):
    leng = (moo[m] - (m + 3)) // 2
    if N < leng:
        find(m - 1, moo, N)

    N -= leng
    if N <= m + 3:
        if N == 1:
            print('m')
        else:
            print('o')
        exit()
    else:
        N -= m + 3
        find(m - 1, moo, N)


N = int(input())

moo = [3]

m = 0
for k in range(1, N + 1):
    if moo[k - 1] >= N:
        m = k - 1
        break
    moo.append(moo[k - 1] * 2 + k + 3)

find(m, moo, N)
