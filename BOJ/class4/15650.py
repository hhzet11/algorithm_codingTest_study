from itertools import combinations
n, m = map(int, input().split())
result = list(combinations(range(1, n+1), m))
for r in result :
    print(*r)