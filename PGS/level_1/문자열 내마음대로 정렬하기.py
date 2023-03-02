def solution(strings, n):
    # 1차 풀이 - 성공
    strings.sort(key = lambda x: (x[n], x))
    return strings