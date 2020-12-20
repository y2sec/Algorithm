# 17389 보너스 점수

N = int(input())
S = input()
result = 0
bonus = 0
# 조건에 따라 보너스 점수를 부여
for i in range(1, len(S) + 1):
    if S[i-1] == 'O':
        result += i
        result += bonus
        bonus += 1
    else:
        bonus = 0
print(result)
