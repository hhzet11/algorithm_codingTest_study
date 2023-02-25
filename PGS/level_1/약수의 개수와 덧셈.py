def solution(left, right):
    # 1차 풀이 - 성공
    answer = 0
    for i in range(left, right + 1):
        num = 0
        for j in range(1, i+1):
            if i % j == 0:
                num += 1
        if num % 2 == 0 :
            answer += i
        else:
            answer -= i
    return answer

    # 다른 사람 풀이
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer