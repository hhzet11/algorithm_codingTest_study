def solution(dartResult):
    # 1차 풀이 - 런타임 에러
    score = [0, 0, 0, 0]
    cnt = 0
    strList = []
    for i in range(len(list(dartResult))):
        if i != 0 and dartResult[i].isdigit() and dartResult[i-1].isdigit() :
            #strList[i-1] += dartResult[i]
            # 2차 풀이 - 성공
            strList[len(strList) - 1] += dartResult[i]
        else :
            strList.append(dartResult[i])
    for i in strList :
        if i.isdigit() :
            cnt += 1
            score[cnt] += int(i)
        elif i.isalpha() :
            if i == 'D' :
                score[cnt] **= 2
            elif i == 'T' :
                score[cnt] **= 3
        else :
            if i == '*' :
                score[cnt -1] *= 2
                score[cnt] *= 2
            else :
                score[cnt] = int(-score[cnt])
    return sum(score)

    # 다른 사람 풀이
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer