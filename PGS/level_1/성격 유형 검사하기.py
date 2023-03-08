from itertools import islice
def solution(survey, choices):
    # 1차 풀이 - 성공
    score = [3, 2, 1, 0, 1, 2, 3]
    type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i, j in zip(survey, choices) :
        if j > 4 :
            type[i[1]] += score[j-1]
        else :
            type[i[0]] += score[j-1]
    answer = ''
    while len(type) > 0 :
        sub = dict(islice(type.items(), 2))
        sub = sorted(sub.items(), key = lambda item: item[1], reverse = True)
        answer += sub[0][0]
        type.pop(sub[0][0])
        type.pop(sub[1][0])
    return answer

    # 다른 사람 풀이
    my_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for A, B in zip(survey, choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B - 4
        else:
            my_dict[A] += B - 4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result