# 1차 시도 - 실패
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    b1, b2, w = map(int, input().split())
    bus[b1].append((b2, w))

def dijkstra(bus, start):
    distances = [int(1e9)] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue :
        dist, node = heapq.heappop(queue)
        if distances[node] < dist :
            continue
        for nnode, ndist in bus[node]:
            distance = dist + ndist
            if distance < distances[nnode]:
                distances[nnode] = distance
                heapq.heappush(queue, [distance, nnode])
    return distances

for i in range(1, n+1) :
    result = dijkstra(bus, i)
    for r in range(1, len(result)):
        print(result[r], end = ' ')
    print()

# 다른 사람 풀이
import sys
INF = int(1e9)

n = int(sys.stdin.readline())  # 도시의 수
m = int(sys.stdin.readline())  # 버스의 수

graph = [[INF] * (n + 1) for _ in range(n + 1)]    # 모든 최단 거리를 저장
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기

# 2. 다이나믹 프로그래밍
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()