# input 느리기 때문에 시간 초과되면, sys.stdin.readline()으로 수정해보기
'''
num = int(sys.stdin.readline())
arr = []
for _ in range(num):
    word = sys.stdin.readline().strip()
    if word not in arr:
        arr.append(word)

arr.sort()
temp = ''
for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        if len(arr[i]) > len(arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in arr :
    print(i)
'''
import sys
num = int(sys.stdin.readline())
arr = []
for _ in range(num):
    arr.append(sys.stdin.readline().strip())
set_arr = set(arr)
arr = list(set_arr)
arr.sort() #알파벳 순
arr.sort(key = len) #길이 순

for i in arr :
    print(i)