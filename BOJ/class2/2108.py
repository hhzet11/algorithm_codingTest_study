import operator
from collections import Counter

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num = sorted(num)

# 산술평균
print(round(sum(num)/n))

# 중앙값
if n == 1:
    print(num[0])
    print(num[0])
else:
    print(num[(n-1)//2])
    # 최빈값
    cnt = Counter(num)
    common = cnt.most_common(2)
    if common[0][1] == common[1][1]:
        print(common[1][0])
    else :
        print(common[0][0])

# 범위
print(num[-1] - num[0])
