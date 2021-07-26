# 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    proceed = {name : 0 for name in enroll}
    proceed['-'] = 0

    parent = {enroll[idx] : referral[idx] for idx in range(len(enroll))}
    parent['-'] = None

    for idx in range(len(seller)):
        currentPeople = seller[idx]
        currentAmount = amount[idx] * 100

        while parent[currentPeople] is not None and currentAmount != 0:
            parentAmount = currentAmount // 10
            proceed[currentPeople] += (currentAmount - parentAmount)

            currentPeople = parent[currentPeople]
            currentAmount = parentAmount

    return [proceed[name] for name in enroll]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
