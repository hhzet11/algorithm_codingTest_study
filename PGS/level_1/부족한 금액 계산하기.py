def solution(price, money, count):
    # 1차 풀이 - 성공
    answer = money
    for i in range(0, count+1):
        answer -= price * i
    if answer < 0 :
        return abs(answer)
    else :
        return 0
    
    # 수정본
    return min(abs(answer), 0)

    # 다른 사람 풀이
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))
