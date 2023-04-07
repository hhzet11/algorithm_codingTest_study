import itertools
def solution(k, dungeons):
    # 1차 시도 - 성공
    challenges = list(itertools.permutations(dungeons, len(dungeons)))
    result = 0
    for challenge in challenges:
        answer, num = 0, k
        for c in challenge:
            if c[0] <= num :
                num -= c[1]
                answer += 1
        result = max(result, answer)
    return result