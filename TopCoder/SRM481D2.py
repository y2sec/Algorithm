# SRM481D2 BatchSystem

# duration = [400, 100, 100, 100]
# user = ['Danny Messer', 'Stella Bonasera', 'Stella Bonasera', 'Mac Taylor']

duration = [200, 200, 200]
user = ['Gil', 'Sarah', 'Warrick']

# duration = [100, 200, 50]
# user = ['Horatio Caine', 'horatio caine', 'YEAAAAAAH']

userNum = dict()

for i in range(len(user)):
    if user[i] in userNum:
        userNum[user[i]] += duration[i]
    else:
        userNum[user[i]] = duration[i]

lst = []

for i in range(len(duration)):
    lst.append((user[i], i, duration[i], userNum[user[i]]))

lst.sort(key=lambda x: (x[2], x[3], x[0]))

result = []

for data in lst:
    result.append(data[1])

print(result)
