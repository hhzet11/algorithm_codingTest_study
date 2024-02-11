from collections import deque
import copy

n, m, k = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

dice = [1, 2, 3, 4, 5, 6]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(num):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if num == 0 :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif num == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    elif num == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif num == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

def score(a, b):
    cnt = 0
    queue = deque()
    queue.append((a, b))
    num = graph[a][b]
    tmp_graph = copy.deepcopy(graph)

    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if tmp_graph[nx][ny] == num :
                tmp_graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return max(cnt, 1)

x, y = 0, 0
direction = 0
result = 0
for i in range(k):
    # 위치 이동
    x += dx[direction]
    y += dy[direction]
    # 이동 방향에 칸이 없다면, 반대로 방향 돌리기
    if x < 0 or x >= n or y < 0 or y >= m :
        direction = (direction + 2) % 4
        x += (dx[direction] * 2)
        y += (dy[direction] * 2)

    # 주사위 굴리기
    turn(direction)

    # b와 비교해 이동 방향 결정
    b = graph[x][y]
    a = dice[5]
    # 도착한 칸의 점수 획득
    result += (score(x, y) * b)

    if a > b :
        direction = (direction + 1) % 4
    elif a < b :
        direction = (direction + 3) % 4

print(result)