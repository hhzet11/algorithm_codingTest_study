import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m , r = map(int, input().split())
arr = [0] + list(map(int, input().split()))
#items = [0] + [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(n+1)]
for _ in range(r) :
    h1, h2, w = map(int, input().split())
    graph[h1].append((h2, w))
    graph[h2].append((h1, w))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    D[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if D[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

ans = 0
for i in range(1, n + 1):
    D = [int(1e9)] * (n + 1)
    dijkstra(i)
    tmp = 0
    for d in range(1, n + 1):
        if m >= D[d]:
            tmp += arr[d]

    ans = max(ans, tmp)

print(ans)
# 1차 풀이 - 잘돌아가는데 틀림 : bfs vs dijkstra의 차이를 모르겠음!
# def bfs(start):
#     visit = [-1] * (n+1)
#     visit[start] = 0
#     queue = deque()
#     queue.append(start)
#     maxVal = arr[start-1]
#
#     while queue:
#         t = queue.popleft()
#         for e, w in graph[t] :
#             if visit[e] == -1 and visit[t] + w <= m:
#                 visit[e] = visit[t] + w
#                 maxVal += arr[e-1]
#                 queue.append(e)
#     return maxVal
#
# val = 0
# for i in range(1, n+1):
#     val = max(val, bfs(i))
# print(val)
