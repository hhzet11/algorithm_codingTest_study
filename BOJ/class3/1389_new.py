from collections import deque

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
                print(num)
                print(queue)
    return sum(num)

n, m = map(int, input().split())
friend = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    friend[i].append(j)
    friend[j].append(i)

result = []
for i in range(1, n+1):
    result.append(bfs(friend, i))
print(result.index(min(result))+1)