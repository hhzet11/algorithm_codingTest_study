from collections import deque

n = int(input())
pair = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(pair):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

def bfs(start):
    visit = [-1] * (n+1)
    q = deque()
    q.append(start)
    visit[start] = 0
    cnt = 0

    while q:
        t = q.popleft()
        #print(t)
        for e in graph[t]:
            if visit[e] == -1:
                visit[e] = 0
                q.append(e)
                cnt += 1
    return cnt

cnt = bfs(1)
print(cnt)