from collections import deque

m, n = map(int, input().split())
box = []
queue = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 1:
            queue.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append([nx, ny])

day = 0
for i in box:
    day = max(day, max(i))
    if 0 in i :
        print(-1)
        exit(0)
print(day-1)

