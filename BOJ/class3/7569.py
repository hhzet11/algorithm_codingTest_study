import sys
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