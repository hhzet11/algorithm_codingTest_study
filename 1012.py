from collections import deque
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find(arr, a, b):
    queue = deque()
    queue.append((a,b))
    arr[a][b] = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue
            if arr[nx][ny] == 1 :
                arr[nx][ny] = 0
                queue.append((nx, ny))
    return


for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k) :
        y, x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 1 :
                find(arr, a, b)
                cnt += 1
    print(cnt)