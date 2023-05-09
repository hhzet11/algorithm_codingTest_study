import heapq
v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v) :
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) // 2) :
        tree[arr[0]].append((arr[i*2 -1], arr[i*2]))

# 실패 : 시간초과
def dijkstra(tree, start) :
    distances = [int(1e9)] * (v+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue :
        dist, node = heapq.heappop(queue)
        if distances[node] < dist :
            continue
        for nnode, ndist in tree[node] :
            distance = dist + ndist
            if distance < distances[nnode] :
                distances[nnode] = distance
                heapq.heappush(queue, [distance, nnode])
    return distances[1:]

cost = 0
for i in range(1, v+1) :
    cost = max(cost, max(dijkstra(tree, i)))
print(cost)

# 다른 사람 코드
from collections import deque
def bfs(start) :
    visit = [-1] * (v+1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que :
        t = que.popleft()
        for e, w in tree[t] :
            if visit[e] == -1 :
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e] :
                    _mx = visit[e], e
    return _max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)


