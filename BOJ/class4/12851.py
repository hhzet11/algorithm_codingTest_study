from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001
dist = [[-1, 0] for _ in range(MAX)]

n, k = map(int, input().split())
q = deque([n])
dist[n][0] = 0
dist[n][1] = 1

while q:
    x = q.popleft()
    for i in [x-1, x+1, x*2] :
        if 0 <= i < MAX :
            if dist[i][0] == -1 : # 처음 도달한다면
                dist[i][0] = dist[x][0] + 1 # 걸린 시간 저장
                dist[i][1] = dist[x][1] # 경우의 수 저장
                q.append(i)
            elif dist[i][0] == dist[x][0] + 1 : #처음이 아닌데, 최단시간이라면
                dist[i][1] += dist[x][1]

print(dist[k][0])
print(dist[k][1])