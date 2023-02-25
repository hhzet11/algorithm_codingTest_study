def solution(n):
    # 1차 풀이 - 성공
    if n % 2 == 0 :
        return '수박' * int(n//2)
    else :
        return '수박' * int(n//2) + '수'

    # 다른 사람 풀이
    return "수박" * (n // 2) + "수" * (n % 2)