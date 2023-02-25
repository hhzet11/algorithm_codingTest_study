def solution(absolutes, signs):
    # 1차 풀이 - 성공
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True :
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer

    # 다른 사람 풀이
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer
