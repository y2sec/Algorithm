# 베스트앨범

def solution(genres, plays):
    answer = []

    genre = dict()
    play = dict()

    for idx in range(len(genres)):
        if genres[idx] in genre:
            genre[genres[idx]].append((idx, plays[idx]))
            play[genres[idx]] += plays[idx]
        else:
            genre[genres[idx]] = [(idx, plays[idx])]
            play[genres[idx]] = plays[idx]

    res = sorted(play.items(), key=lambda x: x[1], reverse=True)
    for x, y in res:
        genre[x].sort(key=lambda x: (-x[1], x[0]))
        cnt = 0
        for z in genre[x]:
            if cnt == 2:
                break
            answer.append(z[0])
            cnt += 1

    return answer