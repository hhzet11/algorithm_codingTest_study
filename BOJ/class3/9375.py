import sys
from collections import Counter

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n) :
        name, wear = map(str, sys.stdin.readline().split())
        arr.append(wear)
    num = 1
    result = Counter(arr)
    for i in result :
        num *= result[i] + 1
    print(num - 1)