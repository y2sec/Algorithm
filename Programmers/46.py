# 뉴스 클러스터링

def solution(str1, str2):
    answer = 0
    strs = [str1, str2]
    strMaps = [dict(), dict()]

    for mapIdx in range(len(strMaps)):
        for index in range(len(strs[mapIdx])-1):
            element = strs[mapIdx][index:index + 2].upper()
            if not element.isalpha():
                continue

            if element in strMaps[mapIdx]:
                strMaps[mapIdx][element] += 1
                continue
            strMaps[mapIdx][element] = 1

    intersection = 0
    union = 0

    for element in strMaps[0].keys():
        if element in strMaps[1]:
            intersection += min(strMaps[0].get(element), strMaps[1].get(element))
            union += max(strMaps[0].get(element), strMaps[1].get(element))
            continue
        union += strMaps[0].get(element)

    for element in strMaps[1].keys():
        if element not in strMaps[0]:
            union += strMaps[1].get(element)

    return int(intersection / union * 65536) if union else 65536


print(solution('FRANCE', 'french'))
