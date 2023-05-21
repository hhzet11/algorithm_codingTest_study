from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001
dist = [0] * MAX
move = [0] * MAX

n, k = map(int, input().split())
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k :
            print(dist[k])
            arr = []
            temp = x
            for _ in range(dist[x] + 1):
                arr.append(temp)
                temp = move[temp]
            print(' '.join(map(str, arr[::-1])))
            return x
        for i in [x-1, x+1, x*2] :
            if 0 <= i < MAX and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x
bfs()