import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m) :
    n1, n2, w = map(int, input().split())
    arr[n1].append((n2, w))
start, end = map(int, input().split())

def dijkstra():
    visited = [int(1e9)] * (n+1)
    visited[start] = 0
    move = [0 for _ in range(n+1)]
    queue = []
    heapq.heappush(queue, [visited[start], start])

    while queue :
        dist, node = heapq.heappop(queue)
        if visited[node] < dist :
            continue
        for nnode, ndist in arr[node] :
            distance = dist + ndist
            if distance < visited[nnode] :
                visited[nnode] = distance
                heapq.heappush(queue, [distance, nnode])
                move[nnode] = node
    return visited, move

visit, moving = dijkstra()
print(visit[end])
route = []
temp = end
for _ in range(visit[end] + 1):
    if temp != 0 :
        route.append(temp)
        temp = moving[temp]
print(len(route))
print(' '.join(map(str, route[::-1])))