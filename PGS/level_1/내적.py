def solution(a, b):
    # 1차 풀이 - 성공
    answer = 0
    for i in range(len(a)) :
        answer += a[i] * b[i]
    return answer

    # 다른 사람 풀이
    return sum([x*y for x, y in zip(a, b)])