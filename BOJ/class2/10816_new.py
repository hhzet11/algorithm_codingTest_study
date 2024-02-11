from collections import Counter

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

result = []
card = Counter(nlist)
for i in arr:
    if i in card:
        result.append(card[i])
    else:
        result.append(0)

for i in result:
    print(i, end = ' ')