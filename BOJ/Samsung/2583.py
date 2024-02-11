from collections import deque
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = -1
    cnt = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            if graph[nx][ny] == 0 :
                cnt += 1
                queue.append((nx, ny))
                graph[nx][ny] = -1
    result.append(cnt)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 :
            bfs(i, j)

print(len(result))
for i in sorted(result):
    print(i, end = ' ')

