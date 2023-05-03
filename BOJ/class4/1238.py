import heapq
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(graph, start) :
    distances = [int(1e9)] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue :
        dist, node = heapq.heappop(queue)
        if distances[node] < dist :
            continue
        for nnode, ndist in graph[node] :
            distance = dist + ndist
            if distance < distances[nnode] :
                distances[nnode] = distance
                heapq.heappush(queue, [distance, nnode])

    return distances

cost = []
for i in range(1, n+1) :
    if i == x :
        continue
    start, end = i, x
    result = dijkstra(graph, start)[end] + dijkstra(graph, end)[start]
    cost.append(result)
print(max(cost))


