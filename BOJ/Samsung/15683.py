import copy

n, m = map(int, input().split())
board = []
cctv = []
mode = [[], [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]],]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5] :
            cctv.append([data[j], i, j])

def fill(board, mode, x, y):
    for i in mode :
        nx = x
        ny = y
        while True :
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                break
            if board[nx][ny] == 6 :
                break
            elif board[nx][ny] == 0 :
                board[nx][ny] = 7

def dfs(depth, board):
    global min_val
    if depth == len(cctv) :
        count = 0
        for i in range(n):
            count += board[i].count(0)
        min_val = min(count, min_val)
        return

    tmp_graph = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num] :
        fill(tmp_graph, i, x, y)
        dfs(depth+1, tmp_graph)
        tmp_graph = copy.deepcopy(board)

min_val = int(1e9)
dfs(0, board)
print(min_val)

