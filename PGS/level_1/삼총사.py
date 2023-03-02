from itertools import combinations
def solution(number):
    # 1차 시도 - 성공
    answer = 0
    for comb in combinations(number, 3) :
        sum = 0
        for i in comb :
            sum += i
        if sum == 0 :
            answer += 1
    return answer

    # 다른 사람 풀이
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt