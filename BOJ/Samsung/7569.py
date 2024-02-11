from collections import deque
import sys
m, n, h = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
tomato = []

day = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
def bfs():
    while True:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >=h or ny >= n or nz >= m:
                continueimport sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    arr.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while queue :
    x, y, z = queue.popleft()

    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and arr[a][b][c] == 0 :
            queue.append([a, b, c])
            arr[a][b][c] = arr[x][y][z] + 1
day = 0
for i in arr :
    for j in i :
        for k in j :
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day -1)

            if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == False :
                queue.append((nx, ny, nz))
                box[nx][ny][nz] = box[x][y][z] + 1
                visited[nx][ny][nz] = True

# 모두 1이 아닐 경우
for a in range(h):
    for b in range(n):
        for c in range(m):
            if box[a][b][c] == 1 and visited[a][b][c] == False :
