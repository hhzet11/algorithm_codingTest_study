def solution(x):
    # 1차 풀이 - 성공
    num_sum = sum(list(map(int, str(x))))
    if x % num_sum == 0:
        answer = True
    else:
        answer = False
    return answer

    # 다른 사람 풀이
    # return n%sum(int(x) for x in str(n)) == 0