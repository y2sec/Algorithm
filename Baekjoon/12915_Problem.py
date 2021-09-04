# 12915 대회 개최

E, EM, M, MH, H = map(int, input().split())
E += EM
H += MH

while EM > 0 or MH > 0:
    if max(E, H) >= M >= min(E, H):
        break

    if max(E, H) <= M:
        break

    if (E > H and EM > 0) or MH <= 0:
        M += 1
        E -= 1
        EM -= 1
        continue

    if (E < H and MH > 0) or EM <= 0:
        M += 1
        H -= 1
        MH -= 1
        continue

    if E == H:
        if EM >= MH:
            E -= 1
            EM -= 1
        else:
            H -= 1
            MH -= 1
        M += 1


print(min(E, M, H))
