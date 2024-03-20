from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0 #첫위치도 방문처리 해야함!!

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1 #이동거리 더해주기
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 0 #0이면 못지나가니까 다시 처리해주기

visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1 :
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 :
            print(0, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()