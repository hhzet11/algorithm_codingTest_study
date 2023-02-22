def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(start):
    queue = [start]
    visited[start] = 0
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)
dfs(v)
print("")
bfs(v)

'''
import copy
def dfs(graph, arr) :
    val = arr[0]
    idx = 0
    while True:
        if len(graph[val]) == 0 and idx == 0:
            break
        elif len(graph[val]) == 0 and idx != 0:
            idx -= 1
            val = arr[idx]
        else :
            if graph[val][0] in arr :
                graph[val].pop(0)
            else :
                arr.append(graph[val][0])
                graph[val].pop(0)
                idx += 1
                val = arr[idx]

def bfs(graph2, arr2) :
    val = arr2[0]
    idx = 0
    while True:
        if graph2[val][0] in arr2:
            graph2[val].pop(0)
        else:
            arr2.append(graph2[val][0])
            graph2[val].pop(0)

        if len(graph2[val]) == 0 and len(arr2) != len(node):
            idx += 1
            val = arr2[idx]
        elif len(arr2) == n :
            break
        else :
            break

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
node = []
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    if start not in node :
        node.append(start)
    if end not in node :
        node.append(end)

for i in graph :
    i = i.sort()

graph2 = copy.deepcopy(graph)
dfs_arr = []
dfs_arr.append(v)
dfs(graph, dfs_arr)
for i in dfs_arr:
    print(i, end = ' ')
print()

bfs_arr = []
bfs_arr.append(v)
bfs(graph2, bfs_arr)
for i in bfs_arr:
    print(i, end = ' ')
'''