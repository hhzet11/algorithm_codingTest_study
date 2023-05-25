import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append([0, 0])
    ch = [[-1] * m for _ in range(n)]
    ch[0][0] = 0

    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if ch[nx][ny] == -1 :
                    if arr[nx][ny] >= 1:
                        arr[nx][ny] += 1
                    else :
                        ch[nx][ny] = 0
                        queue.append([nx, ny])

while True :
    bfs()
    flag = 0

    for i in range(n) :
        for j in range(m):
            if arr[i][j] >= 3 :
                arr[i][j] = 0
                flag = 1
            elif arr[i][j] == 2 :
                arr[i][j] = 1
    if flag == 1 :
        time += 1
    else :
        break
print(time)