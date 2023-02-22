import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
arr_dict = {}
for i in range(n):
    pk = sys.stdin.readline().rstrip()
    arr.append(pk)
    arr_dict[pk] = i + 1

for i in range(m):
    word = sys.stdin.readline().strip()
    if word.isdigit() :
        print(arr[int(word)-1])
    else :
        print(arr_dict[word])