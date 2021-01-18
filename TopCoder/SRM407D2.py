# SRM407D2 CorporationSalary

def dfs(salary):
    if dp[salary] == 0:
        if 'Y' not in relations[salary]:
            dp[salary] = 1
        else:
            for i in range(len(relations)):
                if relations[salary][i] == 'Y':
                    if dp[i] == 0:
                        dp[salary] += dfs(i)
                    else:
                        dp[salary] += dp[i]
    return dp[salary]


# relations = ['N']
# relations = ['NNYN', 'NNYN', 'NNNN', 'NYYN']
# relations = ['NNNNNN', 'YNYNNY', 'YNNNNY', 'NNNNNN', 'YNYNNN', 'YNNYNN']
# relations = ['NYNNYN', 'NNNNNN', 'NNNNNN', 'NNYNNN', 'NNNNNN', 'NNNYYN']
relations = ['NNNN', 'NNNN', 'NNNN', 'NNNN']

dp = [0 for _ in range(len(relations))]

for s in range(len(relations)):
    dfs(s)

print(sum(dp))
