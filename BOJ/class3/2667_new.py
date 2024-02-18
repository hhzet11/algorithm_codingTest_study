from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

q = deque()
visited = [[0]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0 :
            q.append((i, j))
            visited[i][j] = 1
            cnt = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)

