import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

pro = list(combinations_with_replacement(arr, m))
for p in pro :
    for i in p :
        print(i, end = ' ')
    print()
