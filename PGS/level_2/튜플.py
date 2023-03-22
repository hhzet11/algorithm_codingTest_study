import re
def solution(s):
    # 1차 시도 - 성공
    s = list(map(str, s[1:-2].split('}')))
    answer = []
    for i in s:
        i = re.sub('[{}]', '', i)
        i = i.lstrip(',')
        answer.append(i)
    answer.sort(key=len)

    final = []
    for i in answer:
        for j in i.split(','):
            if int(j) not in final:
                final.append(int(j))

    return final

# 다른 사람 풀이
from collections import Counter
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
