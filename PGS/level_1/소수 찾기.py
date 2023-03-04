import math
def solution(n):
    # 1차 풀이 - 시간 초과
    answer = n-1
    for i in range(2, n+1):
        for j in range(2, i):
            print(i, j, answer)
            if i % j == 0 :
                answer -= 1
                break
    return answer

    # 2차 풀이 - 성공
    answer = n - 1
    for i in range(2, n + 1):
        # 다른 사람 풀이
        # for j in range(2, int(i**0.5 + 1)):
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                answer -= 1
                break
    return answer

    # 다른 사람 풀이
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)