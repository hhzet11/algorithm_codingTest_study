def solution(num):
    # 1차 풀이 - 성공
    answer = 0
    while num > 0:
        if answer < 500 and num == 1:
            break

        elif answer == 500 :
            answer = -1
            break

        else :
            answer += 1
            if num % 2 == 0:
                num /= 2
            else :
                num = num * 3 + 1
    return answer

    # 다른 사람 풀이
    for i in range(501):
        if num == 1:
            return i
        num = num / 2 if num % 2 == 0 else num * 3 + 1
    return -1