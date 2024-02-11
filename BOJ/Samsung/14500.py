def dfs(x, y, idx, total):
    global answer
    if answer >= total + max_val * (3 - idx):
        return
    if idx == 3:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(x, y, idx + 1, total + arr[nx][ny])
                    visit[nx][ny]= 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visit[nx][ny] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visit = [([0] * m) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
max_val = max(map(max, arr))