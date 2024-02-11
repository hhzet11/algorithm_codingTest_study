n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[r][c] = -1
result = 1
while graph[r][c] != 1:
    temp = False
    # 주변 4칸 확인하기
    for i in range(4):
        d -= 1
        if d == -1 :
            d = 3
        nx = r + dx[d]
        ny = c + dy[d]
        if graph[nx][ny] == 0 :
            r = nx
            c = ny
            result += 1
            graph[r][c] = -1
            temp = True
            break
    if not temp :
        r += dx[d-2]
        c += dy[d-2]

print(result)