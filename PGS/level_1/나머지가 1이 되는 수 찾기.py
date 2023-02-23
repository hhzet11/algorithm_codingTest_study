def solution(n):
    # 1차 풀이 - 성공
    for i in range(2, n):
        if n % i == 1:
            return i