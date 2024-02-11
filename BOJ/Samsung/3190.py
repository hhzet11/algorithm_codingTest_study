from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2 #사과 위치 2

l = int(input())
change = dict()
for i in range(l):
    t, d = input().split()
    change[int(t)] = d

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
queue.append((0, 0))

def turn(d):
    global direction
    if d == 'D':
        direction = (direction+1) % 4
    else :
        direction = (direction-1) % 4

while True :
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n : # 벽에 닿으면 끝
        break
    if graph[x][y] == 2 :
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in change :
            turn(change[cnt])

    elif graph[x][y] == 0 :
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in change :
            turn(change[cnt])

    else : # 자기 몸에 닿으면 끝
        break

print(cnt)