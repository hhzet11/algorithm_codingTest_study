def solution(cacheSize, cities):
    # 1차 풀이 - 성공
    answer = 0
    cache = []
    for c in cities :
        c = c.lower()
        if cacheSize == 0 :
            answer = len(cities) * 5
        elif c not in cache :
            answer += 5
            if len(cache) == cacheSize :
                cache.pop(0)
                cache.append(c)
            else :
                cache.append(c)
        else :
            answer += 1
            cache.remove(c)
            cache.append(c)
    return answer