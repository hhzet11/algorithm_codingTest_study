def solution(N, stages):
    # 1차 풀이 - 성공
    fail = [0] * (N + 1)
    answer = {}
    for i in stages :
        fail[i-1] += 1
    for i in range(len(fail) - 1) :
        if sum(fail[i+1:]) != 0 :
            fail[i] = fail[i] / sum(fail[i+1:])
    fail.pop()
    for i, j in enumerate(fail) :
        answer[i+1] = j
    answer = dict(sorted(answer.items(), key = lambda x : x[1] , reverse = True))
    return list(answer.keys())