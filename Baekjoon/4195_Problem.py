# 4195 친구 네트워크

# union-find 알고리즘을 통해 연결되어 있는지 확인
def find(friend):
    if friend == network[friend]:
        return friend
    else:
        network[friend] = find(network[friend])
        return network[friend]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        network[b_parent] = a_parent
        number[a_parent] += number[b_parent]


test_case = int(input())

for x in range(test_case):
    F = int(input())
    network = dict()
    number = dict()
    
    # 입력 받은 친구 네트워크를 dict를 이용하여 저장 후 속해있는 인원을 출력
    for y in range(F):
        friendA, friendB = input().split()
        if friendA not in network:
            network[friendA] = friendA
            number[friendA] = 1
        if friendB not in network:
            network[friendB] = friendB
            number[friendB] = 1

        union(friendA, friendB)
        print(number[find(friendA)])
