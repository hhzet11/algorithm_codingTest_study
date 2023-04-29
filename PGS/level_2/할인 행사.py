# 1차 풀이 - 성공
from collections import Counter
def solution(want, number, discount):
    answer = 0
    wanted = {}
    for i, w in enumerate(want):
        if w not in discount:
            return 0
        else:
            wanted[w] = number[i]
    wanted = sorted(wanted.items(), key=lambda x: x[0])

    for i in range(len(discount) - 9):
        dc = discount[i: i + 10]
        num = sorted(dict(Counter(dc)).items(), key=lambda x: x[0])
        if wanted == num:
            answer += 1

    return answer