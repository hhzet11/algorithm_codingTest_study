from collections import deque

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
queue = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    queue.append(i)
    check = [0 for _ in range(n)]
    
    while queue:
        q = queue.popleft()
        for j in range(n):
            if check[j] == 0 and graph[q][j] == 1:
                queue.append(j)
                check[j] = 1
                visited[i][j] = 1
                
for i in visited:
    for j in i:
        print(j, end = ' ')
    print()

# print(*i) : 리스트의 원소나 문자열 각각의 문자를 한 칸씩 띄운 후 출력