# 1차 풀이 - 실패
def check(computers, a, b, nodes):
    nodes.append(b)
    nodes.append(a)
    computers[a][b] = 0
    computers[b][a] = 0
    if 1 in computers[b]:
        count = computers[b].count(1)
        for i in range(count):
            cnt = computers[b].index(1)
            check(computers, b, cnt, nodes)

def solution(n, computers):
    answer = 0
    for i in range(n):
        computers[i][i] = 0

    nodes = []
    for i, comp in enumerate(computers):
        for j, c in enumerate(comp):
            if c == 1:
                check(computers, i, j, nodes)
                answer += 1

    for i in range(n):
        if i not in set(nodes):
            answer += 1
    return answer


# 다른 사람 풀이 - DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1 and visited[connect] == False:
            DFS(n, computers, connect, visited)