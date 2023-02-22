import sys
n = int(sys.stdin.readline())
arr = []
for _ in range (n) :
    arr.append(list(map(int, sys.stdin.readline().split())))
result = []

def check(x, y, n) :
    color = arr[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != arr[i][j] :
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else :
        result.append(1)

check(0, 0, n)
print(result.count(0))
print(result.count(1))

