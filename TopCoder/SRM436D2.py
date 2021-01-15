# SRM436D2 FriendScore

def solution(friends):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friends[i][j] == 'Y':
                friend[i] += 1
            else:
                for k in range(N):
                    if friends[i][k] == friends[j][k] and friends[i][k] == 'Y':
                        friend[i] += 1
                        break

    return max(friend)


N = int(input())
friends = [input() for _ in range(N)]
friend = [0 for _ in range(N)]

print(solution(friends))
