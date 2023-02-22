def solution(n):
    # 1차 풀이 - 성공
    answer = list(reversed(list(map(int, str(n)))))
    return answer

    # 다른 사람 풀이
    # return list(map(int, reversed(str(n))))