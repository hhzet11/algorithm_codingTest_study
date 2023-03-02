def solution(sizes):
    # 1차 시도 - 성공
    answer = 0
    minVal, maxVal = 1, 1
    for i in sizes :
        if minVal < min(i) :
            minVal = min(i)
        if maxVal < max(i) :
            maxVal = max(i)
    return minVal * maxVal

    # 다른 사람 풀이
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)