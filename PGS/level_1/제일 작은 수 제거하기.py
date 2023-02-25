def solution(arr):
    # 1차 풀이 - 성공
    arr.remove(min(arr))
    if len(arr) > 0 :
        return arr
    else :
        return [-1]