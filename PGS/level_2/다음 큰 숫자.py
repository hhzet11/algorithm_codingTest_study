def solution(n):
    # 1차 풀이 - 성공
    binary = format(n, 'b')
    for i in range(n+1, 2*n) :
        if format(i, 'b').count('1') == binary.count('1') :
            return i