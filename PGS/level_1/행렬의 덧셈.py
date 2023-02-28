def solution(arr1, arr2):
    # 1차 풀이 - 성공
    answer = []
    for i, j in zip(arr1, arr2):
        answer_sum = []
        for a, b in zip(i, j):
            answer_sum.append(a+b)
        answer.append(answer_sum)
    return answer