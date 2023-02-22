def solution(n):
    # 1차 풀이 - 성공
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
    # 다른 사람 풀이
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    # return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])