def solution(cards1, cards2, goal):
    # 1차 풀이 - 성공
    for i in goal :
        if len(cards1) > 0 and i == cards1[0] :
            cards1.pop(0)
        elif len(cards2) > 0 and i == cards2[0] :
            cards2.pop(0)
        else :
            return 'No'
    return 'Yes'

    # 다른 사람 풀이
    idx1, idx2 = 0, 0
    for i in goal :
        if len(cards1) > idx1 and i == cards1[idx1] :
            idx1 += 1
        elif len(cards2) > idx2 and i == cards2[idx2] :
            idx2 += 1
        else :
            return 'No'
    return 'Yes'