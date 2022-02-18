import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = sorted(list(set(arr)))
dict = {}
j = 0
for i in result :
    dict[i] = j
    j+= 1

for i in arr :
    print(dict[i], end = ' ')


