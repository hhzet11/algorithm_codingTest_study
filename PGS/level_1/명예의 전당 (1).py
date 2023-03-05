def solution(k, score):
    # 1차 풀이 - 성공
    minVal, answer = [], []
    for i in score :
        if len(answer) < k :
            minVal.append(i)
            minVal.sort(reverse = True)
        elif minVal[k-1] < i :
            minVal.pop()
            minVal.append(i)
            minVal.sort(reverse = True)
        answer.append(minVal[-1])
    return answer

    # 다른 사람 풀이
    q = []
    answer = []
    for s in score:
        q.append(s)
        # sorting 할 필요 없이 min으로 해결!
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))
    return answer