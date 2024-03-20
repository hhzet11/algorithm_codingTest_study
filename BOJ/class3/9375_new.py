from itertools import product
T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        c = list(map(str, input().split()))
        if c[1] in clothes :
            clothes[c[1]].append(c[0])
        else:
            clothes[c[1]] = [c[0]]

    cnt = 1
    for k in clothes:
        cnt *= (len(clothes[k]) + 1)
    print(cnt - 1)