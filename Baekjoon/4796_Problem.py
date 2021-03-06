# 4796 캠핑

L, P, V = map(int, input().split())
camps = []
while L != 0 or P != 0 or V != 0:
    camp = V // P * L
    camp += min(L, V % P)
    camps.append(camp)

    L, P, V = map(int, input().split())

for i in range(len(camps)):
    print('Case ' + str(i+1) + ':', camps[i])
