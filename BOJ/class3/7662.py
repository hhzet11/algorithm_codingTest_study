import sys
import heapq
input = sys.stdin.readline

T = int(input())
while T > 0 :
    T -= 1
    max_heap, min_heap = [], []
    visit = [False] * 1000001

    k = int(input())
    for i in range(k):
        q, num = map(str, input().split())
        if q == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (int(num) * -1, i))
            visit[i] = True

        elif q == 'D' :
                if int(num) == 1 :
                    while max_heap and not visit[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visit[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                elif int(num) == -1 :
                    while min_heap and not visit[min_heap[0][1]] :
                        heapq.heappop(min_heap)
                    if min_heap :
                        visit[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

    while min_heap and not visit[min_heap[0][1]] :
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else :
        print('EMPTY')