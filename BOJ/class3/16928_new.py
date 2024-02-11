from collections import deque
n, m = map(int, input().split())

stair, snake = {}, {}
for i in range(n):
    x, y = map(int, input().split())
    stair[x] = y
for i in range(m):
    x, y = map(int, input().split())
    snake[x] = y

board = [0 for i in range(101)]
visit = [0 for i in range(101)]

queue = deque([1])
while queue:
    x = queue.popleft()
    if x == 100 :
        print(board[x])
        break
    for i in range(1, 7):
        next = x + i
        if next <= 100 and visit[next] == 0:
            if next in stair.keys():
                next = stair[next]
            if next in snake.keys():
                next = snake[next]
            if visit[next] == 0 :
                visit[next] = 1
                board[next] = board[x] + 1
                queue.append(next)
