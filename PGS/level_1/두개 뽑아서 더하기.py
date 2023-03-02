from itertools import combinations
def solution(numbers):
    # 1차 풀이 - 성공
    answer = []
    for i in combinations(numbers, 2):
        if sum(i) not in answer :
            answer.append(sum(i))
    return sorted(answer)

    # 다른 사람 풀이
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    return sorted(set(answer))