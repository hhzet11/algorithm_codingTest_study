# 1차 풀이 - 성공
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course :
        combi = []
        for order in orders :
            combi += combinations(sorted(order), c)
            #order = sorted(order)
            #combi.append(["".join(i) for i in list(combinations(order, c))])
        #combi = sum(combi, [])
        count = Counter(combi).most_common()

        answer += [k for k, v in count if v > 1 and v == count[0][1]]
        #if len(count)>0 :
        #    maxVal = count[0][1]
        #else : break

        for i in count :
            if i[1] >= 2 and i[1] == maxVal :
                answer.append("".join(i[0]))
                #answer.append(i[0])
    return sorted(answer)