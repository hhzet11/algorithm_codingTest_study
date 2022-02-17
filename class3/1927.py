import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num == 0 :
        if not heap :
            print(0)
        else :
            print(heapq.heappop(heap))
    else :
        heap.heappush(heap, num)
