def solution(s):
    # 1차 풀이 - 성공
    answer = sorted(list(s), reverse = True)
    return ''.join(answer)

    # 다른 사람 풀이
    return ''.join(sorted(s, reverse=True))