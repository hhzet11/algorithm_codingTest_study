from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0
left = []

def bfs():
    q = deque()
    q.append([0, 0])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0
    cnt = 0

    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 0: # 가장자리만 확인하도록 해 시간 단축!
                    visited[nx][ny] = 0
                    q.append([nx, ny])
                elif arr[nx][ny] == 1:
                    # 여기서 q에 넣지 않기 때문에 안쪽의 구멍은 처리하지 않게 됨!
                    arr[nx][ny] = 0
                    visited[nx][ny] = 0
                    cnt += 1
    left.append(cnt)
    return cnt

while True:
    cnt = bfs()
    if cnt == 0 :
        break
    time += 1
print(time)
print(left[-2])