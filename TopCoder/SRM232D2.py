# SRM232D2 StockHistory

# initialInvestment = 1000
# monthlyContributon = 0
# stockPrices = ['10 20 30', '15 24 32']

# initialInvestment = 1000
# monthlyContributon = 0
# stockPrices = ['10', '9']

initialInvestment = 100
monthlyContributon = 20
stockPrices = ['40 50 60', '37 48 55', '100 48 50', '105 48 47', '110 50 52', '110 50 52', '110 51 54', '109 49 53']

data = [[] for _ in range(len(stockPrices[0].split()))]

for prices in stockPrices:
    cnt = 0
    for price in prices.split():
        data[cnt].append(int(price))
        cnt += 1
diffPrices = [data[x][-1] / min(data[x]) for x in range(len(data))]
ans = 0
currMoney = initialInvestment

for i in range(len(stockPrices)-1):
    for j in range(len(data)):
        if max(diffPrices) > 0 and max(diffPrices) == data[j][-1] / data[j][i]:
            ans += currMoney * ((data[j][-1] / data[j][i]) - 1)
            currMoney = 0
            break
    diffPrices = [data[x][-1] / min(data[x][i+1:]) for x in range(len(data))]
    currMoney += monthlyContributon

print(int(ans))
