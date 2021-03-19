# 사은품 교환하기

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    goods = 0
    for seasonCouponNum in range(5, 12):
        while N >= seasonCouponNum and M >= 12 - seasonCouponNum:
            max_goods_N, max_goods_M = N // seasonCouponNum, M // (12 - seasonCouponNum)
            max_goods = min(max_goods_N, max_goods_M)
            goods += max_goods
            N, M = N - (seasonCouponNum * max_goods), M - ((12 - seasonCouponNum) * max_goods)
    goods += (N // 12)
    print(goods)
