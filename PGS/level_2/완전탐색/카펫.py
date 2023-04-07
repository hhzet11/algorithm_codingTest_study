def solution(brown, yellow):
    # 1차 풀이 - 성공
    multiply = []
    by = brown + yellow
    for i in range(3, by):
        if by % i == 0 :
            multiply.append([i, by//i])
    for m in multiply :
        if (m[0]-2) * (m[1]-2) == yellow :
            return [max(m), min(m)]