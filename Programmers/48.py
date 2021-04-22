# 캐시

def solution(cacheSize, cities):
    answer = 0

    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            recently = cache.pop(cache.index(city))
            cache.append(recently)
            answer += 1
            continue

        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)

        answer += 5

    return answer
