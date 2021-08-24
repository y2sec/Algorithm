# 1759 암호 만들기

def makePassword(c, idx, con, vo):
    if len(c) == L:
        if con >= 2 and vo >= 1:
            print(c)
        return

    for i in range(idx, C):
        if char[i] in vowel:
            makePassword(c + char[i], i + 1, con, vo + 1)
        else:
            makePassword(c + char[i], i + 1, con + 1, vo)

    pass


L, C = map(int, input().split())
char = sorted(list(input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']

for idx in range(C - L + 1):
    if char[idx] in vowel:
        makePassword(char[idx], idx + 1, 0, 1)
        continue

    makePassword(char[idx], idx + 1, 1, 0)
