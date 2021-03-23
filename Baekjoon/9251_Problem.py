# 9251 LCS

str1 = input()
str2 = input()
str1_len = len(str1)
str2_len = len(str2)

lcs = [[0] * (str1_len + 1) for _ in range(str2_len + 1)]

for s2 in range(1, str2_len + 1):
    for s1 in range(1, str1_len + 1):
        if str1[s1 - 1] == str2[s2 - 1]:
            lcs[s2][s1] = lcs[s2 - 1][s1 - 1] + 1
        else:
            lcs[s2][s1] = max(lcs[s2][s1 - 1], lcs[s2 - 1][s1])

print(lcs[str2_len][str1_len])