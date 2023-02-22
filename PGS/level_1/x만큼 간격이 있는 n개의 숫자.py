def solution(x, n):
    # 1차 풀이 - 성공
    answer = []
    answer.append(x)
    for i in range(1, n):
        answer.append(answer[i-1] + x)
    return answer

    # 다른 사람 풀이
    # return [i * x + x for i in range(n)]