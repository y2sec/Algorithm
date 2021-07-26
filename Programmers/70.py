# 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    answer = []

    proceed = dict()
    for name in enroll:
        proceed[name] = 0
    proceed['-'] = 0

    parent = dict()
    for idx in range(len(enroll)):
        parent[enroll[idx]] = referral[idx]
    parent['-'] = None

    for idx in range(len(seller)):
        currentPeople = seller[idx]
        currentAmount = amount[idx] * 100

        while parent[currentPeople] is not None and currentAmount != 0:
            parentAmount = currentAmount // 10
            proceed[currentPeople] += (currentAmount - parentAmount)

            currentPeople = parent[currentPeople]
            currentAmount = parentAmount

    for name in enroll:
        answer.append(proceed[name])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
