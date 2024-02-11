from collections import deque
n, m = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R' :
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            #print(rx, ry, bx, by)
            if count > 10 : # 움직인 횟수 10회 초과면 -1출력
                print(-1)
                return
            if graph[rx][ry] == 'O': # 현재 위치 구명이면
                print(count)
                return
            for i in range(4): #4방향 탐색
                nrx, nry = rx, ry # 빨간색의 경우
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#': #벽이면 뒤로 한칸 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                if graph[nbx][nby] == 'O': #파란구슬이 먼저 또는 동시에 들어가면 안되서 무시
                    continue
                if nrx == nbx and nry == nby: #두 구슬 위치 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby-by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited: #방문한 적 없으면
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)
bfs(rx, ry, bx, by)
