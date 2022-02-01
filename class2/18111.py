import sys
n,m,b = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

Min = min(map(min,graph))
Max = max(map(max,graph))
leastTime = 1e9

for i in range(257):
    pluscnt = 0
    minuscnt = 0
    for j in range(n):
        for k in range(m):
            h = graph[j][k] - i
            if h > 0:
                minuscnt += h
            elif h < 0:
                pluscnt -= h
    if minuscnt + b >= pluscnt:
        time = minuscnt*2 + pluscnt
        if leastTime >= time:
            leastTime = time
            resultHeight = i
print(leastTime, resultHeight)
