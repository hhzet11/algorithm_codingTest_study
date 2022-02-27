import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101
ladder = {}
snake = {}

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for move in range(1, 7):
            check = now + move
            if 0 < check <= 100 and not visited[check]:
                if check in ladder.keys():
                    check = ladder[check]
                if check in snake.keys():
                    check = snake[check]
                if not visited[check]:
                    queue.append(check)
                    visited[check] = True
                    board[check] = board[now] + 1

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

bfs()
print(board[100])