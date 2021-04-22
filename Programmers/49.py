# 방금그곡

def solution(m, musicinfos):
    answer = '(None)'
    maxTime = 0

    findmusic = []
    for idx in range(len(m)):
        if m[idx] == '#':
            findmusic[-1] += '#'
            continue
        findmusic.append(m[idx])

    m = ' '.join(findmusic) + ' '

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        melody = []
        for idx in range(len(musicinfo[3])):
            if musicinfo[3][idx] == '#':
                melody[-1] += '#'
                continue
            melody.append(musicinfo[3][idx])

        hour = int(musicinfo[1][:2]) - int(musicinfo[0][:2])
        minute = int(musicinfo[1][3:]) - int(musicinfo[0][3:])

        time = (hour * 60) + minute
        music = ''
        for idx in range(time):
            music += melody[idx % len(melody)] + ' '

        if m in music and time > maxTime:
            maxTime = time
            answer = musicinfo[2]

    return answer