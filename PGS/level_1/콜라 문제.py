def solution(a, b, n):
    # 1차 풀이 - 실패
    result, sub = 0, 0
    while n > 0 :
        if n % a == 0 :
            result += (n // a) * b
            n = n // a
        elif n % a != 0 and n > a :
            result += (n // a) * b
            sub += n % a
            n = n // a
        elif n % a != 0 and sub > 0 :
            sub -= 1
            n += 1
        else :
            break
    return result

    # 2차 풀이 - 성공
    answer = 0
    while n >= a:
        answer += n // a * b
        n = (n // a) * b + (n % a)
    return answer

    # 다른 사람 풀이
