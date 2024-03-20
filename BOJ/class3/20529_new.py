from collections import Counter
from itertools import combinations

def dist(a, b):
    cnt = 0
    for i, j in zip(a, b):
        if i != j:
            cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    n = int(input())
    mbti = list(map(str, input().split()))
    if n > 32:
        print(0)
    else:
        res = 100
        comb = combinations(mbti, 3)
        for a, b, c in comb :
            tmp = 0
            tmp += dist(a, b)
            tmp += dist(b, c)
            tmp += dist(c, a)

            res = min(res, tmp)
        print(res)