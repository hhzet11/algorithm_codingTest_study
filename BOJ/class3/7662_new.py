import sys
import heapq

input = sys.stdin.readline
test = int(input())
for _ in range(test):
    max_heapq, min_heapq = [], []
    visit = [False] * 1_000_001

    order_num = int(input())
    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heapq, (int(order[1]), key))
            heapq.heappush(max_heapq, (int(order[1]) * -1, key))
            visit[key] = True
        elif order[0] == 'D':
            if order[1] == '-1':
                while min_heapq and not visit[min_heapq[0][1]]:
                    heapq.heappop(min_heapq)
                if min_heapq:
                    visit[min_heapq[0][1]] = False
                    heapq.heappop(min_heapq)
            elif order[1] == '1':
                while max_heapq and not visit[max_heapq[0][1]]:
                    heapq.heappop(max_heapq)
                if max_heapq:
                    visit[max_heapq[0][1]] = False
                    heapq.heappop(max_heapq)
        print(key, max_heapq)
        print(key, min_heapq)

    while min_heapq and not visit[min_heapq[0][1]]:
        heapq.heappop(min_heapq)
    while max_heapq and not visit[max_heapq[0][1]]:
        heapq.heappop(max_heapq)

    if min_heapq and max_heapq:
        print(-max_heapq[0][0], min_heapq[0][0])
    else:
        print('EMPTY')