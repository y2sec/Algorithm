# SRM258D2 AutoLoan

# price = 6800
# monthlyPaymemt = 100
# loanTerm = 68

# price = 2000
# monthlyPaymemt = 510
# loanTerm = 4

price = 15000
monthlyPaymemt = 364
loanTerm = 48

minInterestRate = 0
maxInterestRate = 100
midInterestRate = (maxInterestRate + minInterestRate) / 2

ans = 0

while minInterestRate < maxInterestRate:
    cpPrice = price
    for i in range(loanTerm):
        cpPrice *= ((midInterestRate / 1200) + 1)
        cpPrice -= monthlyPaymemt
    if cpPrice == 0 or (maxInterestRate - minInterestRate) <= 1e-9:
        ans = midInterestRate
        break
    elif cpPrice > 0:
        maxInterestRate = midInterestRate
    else:
        minInterestRate = midInterestRate
    midInterestRate = (maxInterestRate + minInterestRate) / 2

print(ans)
