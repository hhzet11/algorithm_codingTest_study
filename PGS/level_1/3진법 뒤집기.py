def solution(n):
    # 1차 풀이 - 성공
    answer_3 = []
    while n > 0 :
        answer_3.append(n%3)
        n = int(n/3)
    answer = ''.join(str(i) for i in answer_3)
    return int(answer, 3)

    # 다른 사람 풀이
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer