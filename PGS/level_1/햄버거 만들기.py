def solution(ingredient):
    # 1차 풀이 - 실패
    answer = 0
    turn = True
    while turn:
        for i in ingredient:
            if i + 4 <= len(ingredient) and ingredient[i:i + 4] == [1, 2, 3, 1]:
                answer += 1
                del ingredient[i:i + 4]
                break
            else:
                turn = False
    return answer

    # 다른 사람 풀이
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt
