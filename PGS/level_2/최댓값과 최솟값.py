def solution(s):
    # 1차 풀이 - 성공
    num = list(map(int, s.split()))
    answer = str(min(num)) + ' ' + str(max(num))
    return answer