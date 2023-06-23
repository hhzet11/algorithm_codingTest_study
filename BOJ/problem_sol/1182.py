import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
total = 0
for i in range(1, n+1):
    combi = combinations(num, i)
    for c in combi :
        if sum(c) == s :
            total += 1
print(total)