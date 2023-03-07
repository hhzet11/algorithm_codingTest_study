def solution(numbers, hand):
    # 1차 풀이 - 성공
    answer = ''
    l, r = 10, 12
    for i in range(len(numbers)) :
        if numbers[i] == 0 :
            numbers[i] = 11

    for i in numbers :
        if i in [1, 4, 7] :
            answer += 'L'
            l = i
        elif i in [3, 6, 9] :
            answer += 'R'
            r = i
        else :
            distL = abs((l-1)%3 - (i-1)%3) + abs((l-1)//3 - (i-1)//3)
            distR = abs((r-1)%3 - (i-1)%3) + abs((r-1)//3 - (i-1)//3)
            if distL > distR :
                r = i
                answer += 'R'
            elif distL <  distR:
                l = i
                answer += 'L'
            else :
                if hand == 'right':
                    r = i
                    answer += 'R'
                else :
                    l = i
                    answer += 'L'
    return answer

    # 다른 사람 풀이
    answer = ''
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
