def solution(n):
    # 2차 풀이 - 성공
    # 제곱근 : ** 0.5
    answer = 0
    num = n ** 0.5
    if num % 1 == 0:
        answer = (num + 1) ** 2
    else:
        answer = -1
    return answer