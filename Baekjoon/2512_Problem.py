# 2512 예산

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

if M >= sum(budgets):
    print(max(budgets))
else:
    minBudget = 0
    maxBudget = max(budgets)
    midBudget = (minBudget + maxBudget) // 2

    result = 0
    while minBudget <= maxBudget:
        sumBudget = 0

        for budget in budgets:
            if midBudget >= budget:
                sumBudget += budget
            else:
                sumBudget += midBudget

        if sumBudget > M:
            maxBudget = midBudget - 1
        else:
            result = max(result, midBudget)
            minBudget = midBudget + 1

        midBudget = (minBudget + maxBudget) // 2

    print(result)
