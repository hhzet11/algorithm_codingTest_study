from collections import deque
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 :
                bfs(i, j)
                graph[i][j] = 0
                cnt += 1

    print(cnt)