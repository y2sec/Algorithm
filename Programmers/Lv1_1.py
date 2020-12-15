# 완주하지 못한 선수

def solution(participant, completion):
    players = dict()
    answer = ''

    # 선수들 이름을 dict에 저장
    for p in participant:
        if p in players:
            players[p] += 1
        else:
            players[p] = 1

    # 완주한 선수를 제외해줌
    for c in completion:
        players[c] -= 1

    # 완주하지 못한 선수가 있으면 answer에 저장
    for player, finished in players.items():
        if finished == 1:
            answer = player
            break

    return answer
