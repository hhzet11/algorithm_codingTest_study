def solution(a, b):
    # 1차 풀이 - 성공
    answer = 0
    max_n, min_n = max((a, b)), min((a, b))
    for i in range(min_n, max_n+1):
        answer += i
    return answer

    # 다른 사람 풀이 1
    '''
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
    '''

    # 다른 사람 풀이 2
    # return sum(range(min(a, b), max(a, b) + 1))