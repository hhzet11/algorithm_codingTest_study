n, m, x, y, k = map(int, input().split())
graph= []
for i in range(n):
    graph.append(list(map(int, input().split())))

dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
d = list(map(int, input().split()))

def turn(num):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if num == 1 :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif num == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif num == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif num == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(k):
    # 위치 이동
    x += dx[d[i] - 1]
    y += dy[d[i] - 1]

    if x < 0 or x >= n or y < 0 or y >= m :
        x -= dx[d[i] - 1]
        y -= dy[d[i] - 1]
        continue

    # 주사위 굴리기
    turn(d[i])

    # 아랫칸 숫자 바꾸기
    if graph[x][y] == 0 :
        graph[x][y] = dice[5]
    else :
        dice[5] = graph[x][y]
        graph[x][y] = 0

    print(dice[0])