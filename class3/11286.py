import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    num = int(input())
    if num != 0 :
        heapq.heappush(arr, (abs(num), num))
    else :
        try :
            print(heapq.heappop(arr)[1])
        except :
            print(0)