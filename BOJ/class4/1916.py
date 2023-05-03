# 1차 풀이 - 실패
# def route(bus, s, e) :
#     cost = 0
#     for b in bus :
#         print(b)
#         if b[0] == s and b[1] != e :
#             cost += b[2]
#             print(s, e, cost)
#             return cost + route(bus, b[1], e)
#         elif b[0] == s and b[1] == e :
#             cost += b[2]
#             print(s, e, cost)
#             return cost
#
# n = int(input())
# m = int(input())
# bus = []
# for _ in range(m) :
#     b = list(map(int, input().split()))
#     bus.append(b)
# bus.sort(key = lambda x:[x[0], x[1]])
#
# start, end = map(int, input().split())
#
# cost = []
# for b in bus :
#     if b[0] == start :
#         cost.append(route(bus, start, end))
# print(cost)
# print(min(cost))

# 다른사람 풀이
import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())

def dijkstra(graph, start) :
    distances = [int(1e9)] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue :
        dist, node = heapq.heappop(queue)
        if distances[node] < dist :
            continue
        for next_node, next_dist in graph[node] :
            distance = dist + next_dist
            if distance < distances[next_node] :
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return distances

dist_start = dijkstra(graph, start)
print(dist_start[end])