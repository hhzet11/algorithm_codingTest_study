import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distances = [INF] * (v+1)

for _ in range(e) :
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

def dijkstra(start) :
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue :
        dist, node = heapq.heappop(queue)
        if distances[node] < dist :
            continue
        for nnode, ndist in graph[node] :
            distance = ndist + dist
            if distance < distances[nnode] :
                distances[nnode] = distance
                heapq.heappush(queue, (distance, nnode))

dijkstra(start)
for i in range(1, v+1) :
    print("INF" if distances[i] == INF else distances[i])