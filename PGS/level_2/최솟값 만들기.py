def solution(A,B):
    # 1차 풀이 - 성공
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i, j in zip(A, B) :
        answer += i*j
    return answer

    # 다른 사람 풀이
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])