import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1) :
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))

def bfs(start):
    visit = [int(INF)] * (n+1)
    visit[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue :
        dist, node = heapq.heappop(queue)
        if dist > visit[node] :
            continue
        for nnode, ndist in graph[node] :
            distance = dist + ndist
            if distance < visit[nnode] :
                visit[nnode] = distance
                heapq.heappush(queue, (visit[nnode], nnode))
    return visit[1:]


# 트리에서 아무 노드 두개를 통해 가장 긴 경로를 구할 때,
# 1. 트리에서 아무 노드나 잡고 그 노드에 대해 가장 먼 노드를 구하여 v1
# 2. v1에 대해 가장 먼 노드를 v2
# 3. v1과 v2사이의 거리가 트리의 지름!

v1List = bfs(1)
v1 = v1List.index(max(v1List))
v2List = bfs(v1+1)
v2 = v2List.index(max(v2List))
print(v2List[v2])