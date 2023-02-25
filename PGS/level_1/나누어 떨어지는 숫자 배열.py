def solution(arr, divisor):
    # 1차 풀이 - 성공
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) > 0 :
        return sorted(answer)
    else:
        return [-1]