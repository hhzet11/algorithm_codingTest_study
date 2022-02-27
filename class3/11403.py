import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

INF = sys.maxsize
def floyd():
    dist = [[INF]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 :
                dist[i][j] = arr[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j] :
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

dist = floyd()
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF :
            print(1, end = ' ')
        else :
            print(0, end = ' ')
    print()