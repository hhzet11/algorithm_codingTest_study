def solution(s):
    # 1차 풀이 - 성공
    p_num, y_num = 0, 0
    for i in s.lower():
        if i == 'p':
            p_num += 1
        elif i == 'y':
            y_num += 1
    if p_num == y_num :
        answer = True
    else :
        answer = False
    return answer

    # 다른 사람 풀이
    # return s.lower().count('p') == s.lower().count('y')