def solution(wallpaper):
    # 1차 풀이 - 성공
    answer = []
    lux, luy, rux, ruy = 50, 50, 0, 0
    cnt = 0
    for wall in wallpaper :
        for i in range(len(wall)) :
            if wall[i] == '#' :
                if lux > cnt:
                    lux = cnt
                if luy > i :
                    luy = i
                if rux < cnt :
                    rux = cnt
                if ruy < i :
                    ruy = i
        cnt += 1
    return [lux, luy, rux +1, ruy+1]

    # 다른 사람 풀이
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
