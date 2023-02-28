def solution(arr):
    # 1차 풀이 - 성공
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0 or answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer
