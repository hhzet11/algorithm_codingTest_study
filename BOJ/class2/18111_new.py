import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []
for i in range(n):
    g = list(map(int, sys.stdin.readline().split()))
    ground.append(g)

result = 1e9
minH = min(map(min, ground))
maxH = min(max(map(max, ground)), 256)

for h in range(minH, maxH+1):
    putcnt = 0
    removcnt = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > h:
                removcnt += ground[i][j] - h
            else :
                putcnt += h - ground[i][j]

    if putcnt > removcnt + b :
        continue

    count = putcnt + removcnt * 2
    if result >= count:
        result = count
        resultH = h
print(result, resultH)

