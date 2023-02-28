def solution(s):
    # 2차 풀이 성공 - 길이 구하는 거 빼먹음
    if len(s) in (4,6) :
        return s.isdecimal()
    else :
        return False