def solution(n):
    # 1차 풀이 - 성공
    num_list = list(map(int, str(n)))
    num_list.sort(reverse = True)
    answer = ''.join(str(i) for i in num_list)
    return int(answer)

    # 다른 사람 풀이
    '''
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
    '''