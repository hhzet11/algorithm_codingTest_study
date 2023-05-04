t = int(input())
while t > 0 :
    t -= 1
    n = int(input())
    graph = []
    for _ in range(2) :
        graph.append(list(map(int, input().split())))

    for i in range(1, n) :
        if i == 1 :
            graph[0][i] += graph[1][0]
            graph[1][i] += graph[0][0]
        else :
            graph[0][i] += max(graph[1][i-2], graph[1][i-1])
            graph[1][i] += max(graph[0][i-2], graph[0][i-1])
    print(max(graph[0][n-1], graph[1][n-1]))