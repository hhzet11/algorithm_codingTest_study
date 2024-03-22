from collections import deque

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    queue = deque()
    queue.append([a, ''])
    visited = [-1 for i in range(10000)]
    visited[a] = 0

    while queue:
        x, command = queue.popleft()
        if x == b :
            print(command)
            break

        d = x * 2 % 10000
        if visited[d] == -1:
            visited[d] = 0
            queue.append([d, command + 'D'])
        s = (s - 1) % 10000
        if visited[s] == -1:
            visited[s] = 0
            queue.append([s, command + 'S'])
        l = x // 1000 + (x % 1000)* 10
        if visited[l] == -1:
            visited[l] = 0
            queue.append([l, command + 'L'])
        r = x // 10 + (x % 10) * 1000
        if visited[r] == -1:
            visited[r] = 0
            queue.append([r, command + 'R'])


