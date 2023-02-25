def solution(numbers):
    # 1차 풀이 - 성공
    answer = 0
    for i in range(1, 10):
        if i not in numbers :
            answer += i
    return answer

    # 다른 사람 풀이
    return 45 - sum(numbers)