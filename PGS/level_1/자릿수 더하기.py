def solution(n):
    # 1차 풀이 - 성공
    answer = 0
    for i in list(str(n)):
        answer += int(i)
    return answer

    # 다른 사람 풀이
    # return sum([int(i) for i in str(number)])