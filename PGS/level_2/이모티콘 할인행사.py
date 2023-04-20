# 1차 풀이 - 성공
from itertools import product
def solution(users, emoticons):
    sale = [40, 30, 20, 10]
    subscript = 0
    ans = [0, 0]
    for s in product(sale, repeat = len(emoticons)) :
        money = 0
        for u in users :
            sum = 0
            for i, e in zip(s, emoticons) :
                if u[0] <= i :
                    sum += int(e * (100 - i) / 100)
            if sum >= u[1] :
                subscript += 1
                sum = 0
            money += sum
        if subscript > ans[0] or (subscript == ans[0] and money > ans[1]) :
            ans = [subscript, money]
        subscript = 0
    return ans