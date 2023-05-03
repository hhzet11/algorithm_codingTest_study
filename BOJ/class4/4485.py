import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra() :
    q = []
    heapq.heappush(q, (df[0][0], 0, 0))
    distance[0][0] = 0

    while q :
        cost, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1 :
            print(f"Problem {count} : {distance[x][y]}")
            break

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                new_cost = cost + df[nx][ny]
                if new_cost < distance[nx][ny] :
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

count = 1
while True :
    n = int(input())
    if n == 0 :
        break

    df = []
    for _ in range(n) :
        df.append(list(map(int, input().split())))
    distance = [[1e9]*n for _ in range(n)]

    dijkstra()
    count += 1

