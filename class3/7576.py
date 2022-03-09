import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 :
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue :
    x, y = queue.popleft()
    for i in range(4) :
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<n and 0<=b<m and arr[a][b] == 0 :
            queue.append([a, b])
            arr[a][b] = arr[x][y] + 1

day = 0
for i in arr :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day -1)