# 1차 풀이 - 실패 : 시간초과
def solution(topping):
    answer = 0
    for i in range(1, len(topping)-1) :
        roll1 = len(set(topping[:i]))
        roll2 = len(set(topping[i:]))
        if roll1 == roll2 :
            answer += 1
    return answer

# 다른 사람 풀이
from collections import Counter
def solution(topping):
    dic = Counter(topping)
    set_dic = set()

    res = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        # dictation에서 value 값이 0이 될 경우, 제외해서 len 개수 맞춰줌 >> 그냥 두면 0도 개수로 셈
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1
    return res