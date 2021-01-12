# SRM478 KiwiJuiceEasy

def solution(capacities, bottles, fromId, toId):
    for i in range(len(fromId)):
        bottles[toId[i]] += bottles[fromId[i]]
        bottles[fromId[i]] = 0

        if capacities[toId[i]] < bottles[toId[i]]:
            bottles[fromId[i]] = bottles[toId[i]] - capacities[toId[i]]
            bottles[toId[i]] = capacities[toId[i]]

    print(bottles)


# 병의 용량, 주스 용량, fromId[i] -> toId[i]

# # T1
# capacities = [20, 20]
# bottles = [5, 8]
# fromId = [0]
# toId = [1]

# # T2
# capacities = [10, 10]
# bottles = [5, 8]
# fromId = [0]
# toId = [1]

# # T3
# capacities = [30, 20, 10]
# bottles = [10, 5, 5]
# fromId = [0, 1, 2]
# toId = [1, 2, 0]
#
# # T4
# capacities = [14, 35, 86, 58, 25, 62]
# bottles = [6, 34, 27, 38, 9, 60]
# fromId = [1, 2, 4, 5, 3, 3, 1, 0]
# toId = [0, 1, 2, 4, 2, 5, 3, 1]

# T5
capacities = [700000, 800000, 900000, 1000000]
bottles = [478478, 478478, 478478, 478478]
fromId = [2, 3, 2, 0, 1]
toId = [0, 1, 1, 3, 2]

solution(capacities, bottles, fromId, toId)
