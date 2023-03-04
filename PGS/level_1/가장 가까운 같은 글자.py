def solution(s):
    # 1차 풀이 - 성공
    newDict, answer = {}, []
    for i in range(len(s)) :
        if s[i] not in newDict :
            newDict[s[i]] = i
            answer.append(-1)
        else :
            answer.append(i - newDict[s[i]])
            newDict[s[i]] = i
    return answer

    # 정리
    newDict, answer = {}, []
    for i in range(len(s)):
        if s[i] not in newDict:
            answer.append(-1)
        else:
            answer.append(i - newDict[s[i]])
         newDict[s[i]] = i
    return answer