def solution(food):
    # 1차 풀이 - 성공
    answer = ''
    for i in range(1, len(food)) :
        if food[i] != 1 :
            answer += str(i) * (food[i] // 2)
    # 다른 사람 풀이
    # return answer + "0" + answer[::-1]
    answer += '0'
    answer += answer[::-1][1:]
    return answer