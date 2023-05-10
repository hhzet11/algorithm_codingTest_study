import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e) :
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

def dijkstra(start):
    visit = [INF] * (v + 1)
    visit[start] = 0
    queue = []
    heapq.heappush(queue, (visit[start], start))

    while queue :
        dist, node = heapq.heappop(queue)
        if visit[node] < dist :
            continue
        for nnode, ndist in graph[node] :
            distance = dist + ndist
            if distance < visit[nnode] :
                visit[nnode] = distance
                heapq.heappush(queue, (distance, nnode))
    return visit

V1, V2 = map(int, input().split())
result = dijkstra(1)
final = dijkstra(V1)
cnt = min(result[V1] + dijkstra(V2)[v], result[V2] + final[v]) + final[V2]
print(cnt if cnt < INF else -1)

