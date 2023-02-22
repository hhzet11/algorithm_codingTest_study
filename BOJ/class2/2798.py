from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
comb = list(combinations(arr, 3))
sum_arr = []
for i in comb :
    sum_arr.append(sum(i))
result = 0
for i in sum_arr :
    if m >= i > result:
        result = i
print(result)