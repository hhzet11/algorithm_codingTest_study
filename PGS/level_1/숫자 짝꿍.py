def solution(X, Y):
    # 1차 풀이 - 시간 초과
    answer = []
    X, Y = list(X), list(Y)
    for i in X :
        if i in Y :
            answer.append(i)
            X.remove(i)
            Y.remove(i)
    if len(answer) > 0 :
        answer.sort(reverse = True)
        if answer[0] == '0' :
            return '0'
        else :
            return ''.join(i for i in answer)
    else :
        return '-1'

    # 다른 사람 풀이
    answer = ''
    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
