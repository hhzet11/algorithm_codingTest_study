def solution(k, m, score):
    # 1차 풀이 - 성공
    answer = 0
    score.sort(reverse = True)
    for i in range(len(score)):
        if i % m == m - 1 :
            answer += score[i] * m
    return answer

    # 다른 사람 풀이
    return sum(sorted(score)[len(score) % m::m]) * m