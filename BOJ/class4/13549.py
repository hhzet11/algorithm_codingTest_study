from collections import deque
MAX = 100001
dist = [-1] * MAX # [-1 for _ in range(MAX)]

n, k = map(int, input().split())
q = deque()
q.append(n)
dist[n] = 0

while q:
    now = q.popleft()
    if now == k :
        print(dist[now])
        break
    if 0 < now*2 < MAX and dist[now*2] == -1:  # 순간이동
        dist[now*2] = dist[now]
        q.appendleft(now * 2)
    if 0 <= now + 1 < MAX and dist[now+1] == -1: # x+1이동
        dist[now+1] = dist[now] + 1
        q.append(now + 1)
    if 0 <= now - 1 < MAX and dist[now-1] == -1: # x-1이동
        dist[now-1] = dist[now] + 1
        q.append(now - 1)