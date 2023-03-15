def solution(s):
    # 1차 풀이 - 성공
    cnt, tmp = 0, 0
    while s != '1' :
        cnt += s.count('0')
        s = s.replace('0', '')
        s = format(int(len(s)), 'b')
        tmp += 1
    return [tmp, cnt]