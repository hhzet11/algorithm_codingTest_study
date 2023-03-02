def solution(array, commands):
    # 1차 풀이 - 성공
    answer = []
    for com in commands :
        i, j, k = com[0], com[1], com[2]
        # 다른 사람 풀이
        # i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer